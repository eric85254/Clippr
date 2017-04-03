"""
    Contains the Models that are utilized by all the apps in the project. Essentially the 'core' models.
"""
from django.contrib.auth.models import AbstractUser
from datetime import datetime as datetime

from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from core.utils.abstract_classes import FullCalendarEvent
from core.utils.picture_locations import DEFAULT_PICTURE_LOCATION, DEFAULT_MENU_PICTURE
from stylist.models import PortfolioHaircut, StylistMenu


class User(AbstractUser):
    """
        Extends the AbstractUser class.
        | Changed the USERNAME_FIELD to be 'email'
        | Modified REQUIRED_FIELDS
        | phone_number is validated by regex
    """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
    username = models.CharField(max_length=1, unique=False, blank=True)

    is_stylist = models.CharField(max_length=3, default="NO")
    profile_picture = models.FileField(upload_to='profile_pictures/%Y/%m/%d', null=True, blank=True,
                                       default=DEFAULT_PICTURE_LOCATION)
    biography = models.TextField(blank=True)
    location = models.TextField(blank=True)
    hair_type = models.TextField(blank=True)
    hidden_hair_type = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15, unique=True)

    # Todo: maybe don't show this until a certain number of people have rated?
    average_stylist_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    average_customer_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)

    def get_portfolio_haircuts(self):
        return PortfolioHaircut.objects.filter(stylist=self)

    def get_stylist_menu(self):
        return StylistMenu.objects.filter(stylist=self)


class GlobalMenu(models.Model):
    """
        Global Menu options available to all stylists are stored here.
    """
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField()

    def __str__(self):
        return self.name


class ItemInBill(models.Model):
    """
        Each ItemInBill is tied to a particular appointment. To get the total cost of the appointment you must
        sum up the ItemInBill.price of all the ItemInBill items that are tied to it.
    """
    item_portfolio = models.ForeignKey('stylist.PortfolioHaircut', related_name='item_portfolio', null=True, blank=True)
    item_menu = models.ForeignKey('stylist.StylistMenu', related_name='item_menu', null=True, blank=True)
    item_custom = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    appointment = models.ForeignKey('core.Appointment', on_delete=models.SET_NULL, null=True)
    charged = models.BooleanField(default=False)

    def __str__(self):
        if (self.item_portfolio == '' or self.item_portfolio is None) is False:
            return str(
                self.appointment.date) + " || stylist: " + self.appointment.stylist.username + " || " + self.item_portfolio.name
        elif (self.item_custom == '' or self.item_custom is None) is False:
            return str(self.appointment.date) + " || " + self.appointment.stylist.username + " || " + self.item_custom
        else:
            return "Unknown Entry"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.item_portfolio is not None and self.item_portfolio != '':
            self.price = self.item_portfolio.price

        elif self.item_menu is not None and self.item_menu != '':
            self.price = self.item_menu.price
            
        super(ItemInBill, self).save()


class Review(models.Model):
    """
        Tied to an appointment. There exists a field for both stylist and customer ratings.
    """
    stylist_rating = models.IntegerField(null=True)
    customer_rating = models.IntegerField(null=True)
    appointment = models.ForeignKey('core.Appointment', related_name='appointment', on_delete=models.SET_NULL,
                                    null=True)


class Appointment(FullCalendarEvent):
    """
        Appointments all have a particular status that describes their current state.
        | They are all tied to a customer and a stylist.
        | An Appointment entry won't be deleted if the stylist or customer is deleted.
    """
    STATUS_PENDING = 'PENDING'
    STATUS_RECHEDULED_BYSTYLIST = 'RESCHEDULED_BYSTYLIST'
    STATUS_RESCHEDULED_BYCUSTOMER = 'RESCHEDULED_BYCUSTOMER'
    STATUS_ACCEPTED = 'ACCEPTED'
    STATUS_DECLINED = 'DECLINED'
    STATUS_COMPLETED = 'STATUS_COMPLETED'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'PENDING'), (STATUS_RECHEDULED_BYSTYLIST, 'RESCHEDULED_BYSTYLIST'),
        (STATUS_RESCHEDULED_BYCUSTOMER, 'RESCHEDULED_BYCUSTOMER'), (STATUS_ACCEPTED, 'ACCEPTED'),
        (STATUS_DECLINED, 'DECLINED'), (STATUS_COMPLETED, 'STATUS_COMPLETED'))

    # Changed it so that record of appointment can't be deleted if any user is deleted.
    # ^ removed on_delete=models.CASCADE. double check to make sure this works.
    stylist = models.ForeignKey('core.User', related_name='stylist', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey('core.User', related_name='customer', on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)

    status = models.TextField(choices=STATUS_CHOICES, default=STATUS_PENDING)

    def item_in_bill(self):
        return ItemInBill.objects.filter(appointment=self)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.status == Appointment.STATUS_COMPLETED:
            self.color = 'green'
        elif self.status == Appointment.STATUS_ACCEPTED:
            self.color = 'blue'
        elif self.status == Appointment.STATUS_RESCHEDULED_BYCUSTOMER or self.status == Appointment.STATUS_RECHEDULED_BYSTYLIST or self.status == Appointment.STATUS_PENDING:
            self.color = 'yellow'
            self.textColor = 'black'

        super(Appointment, self).save()

    def __str__(self):
        return self.stylist.username + "'s appointment with " + self.customer.username


class Application(models.Model):
    """
        Where user's stylists applications are stored.
    """
    applicant = models.ForeignKey('core.User', on_delete=models.CASCADE)
    application_status = models.TextField(default='PENDING')
    denied_reason = models.TextField(blank=True)
    reason = models.TextField()
    interview_time = models.DateTimeField(null=True, blank=True)
    # ToDo: Figure out what fields we want for a stylist application


class Questionnaire(models.Model):
    """
        Model to store any questionnaire's that you want users to fill out.
    """
    question = models.TextField()


class AnsweredQuestionnaire(models.Model):
    """
        Model to store a User's response to a particular questionaire.
        | The current date is also stored.
    """
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    questionnaire = models.ForeignKey('core.Questionnaire', on_delete=models.CASCADE)
    response = models.TextField(blank=True)
    time = models.DateTimeField(default=datetime.now)

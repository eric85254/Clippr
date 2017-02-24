from django.contrib.auth.models import AbstractUser
from datetime import datetime as datetime

from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from core.utils.global_constants import DEFAULT_PICTURE_LOCATION, DEFAULT_MENU_PICTURE


class User(AbstractUser):
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


class Menu(models.Model):
    ADMIN = 'ADMIN'
    STYLIST = 'STYLIST'

    CREATED_BY = ((ADMIN, 'ADMIN'), (STYLIST, 'STYLIST'))

    creator = models.TextField(choices=CREATED_BY, default=ADMIN)
    name = models.CharField(max_length=20)
    # ToDo: should we get rid of category?
    category = models.TextField(default='MAIN')
    # price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # Get rid of the picture field? Pictures are kinda covered by PortfolioHaircuts
    picture = models.FileField(upload_to='menu/%Y/%m/%d', null=True, blank=True, default=DEFAULT_MENU_PICTURE)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Category: " + self.category + " || Option: " + self.name


class ItemInBill(models.Model):
    item_portfolio = models.ForeignKey('stylist.PortfolioHaircut', related_name='item_portfolio', null=True, blank=True)
    item_menu = models.ForeignKey('core.Menu', related_name='item_menu', null=True, blank=True)
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


class Review(models.Model):
    stylist_rating = models.IntegerField(null=True)
    customer_rating = models.IntegerField(null=True)
    appointment = models.ForeignKey('core.Appointment', related_name='appointment', on_delete=models.SET_NULL,
                                    null=True)


class Appointment(models.Model):
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
    date = models.DateTimeField(default=datetime.now)
    price = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)

    status = models.TextField(choices=STATUS_CHOICES, default=STATUS_PENDING)

    def __str__(self):
        return self.stylist.username + "'s appointment with " + self.customer.username


class Application(models.Model):
    applicant = models.ForeignKey('core.User', on_delete=models.CASCADE)
    application_status = models.TextField(default='PENDING')
    denied_reason = models.TextField(blank=True)
    reason = models.TextField()
    interview_time = models.DateTimeField(null=True, blank=True)
    # ToDo: Figure out what fields we want for a stylist application


class Questionnaire(models.Model):
    question = models.TextField()


class AnsweredQuestionnaire(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    questionnaire = models.ForeignKey('core.Questionnaire', on_delete=models.CASCADE)
    response = models.TextField(blank=True)
    time = models.DateTimeField(default=datetime.now)

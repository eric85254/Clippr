from django.contrib.auth.models import AbstractUser
from datetime import datetime as datetime
from django.db import models

# Create your models here.
from core.utils.global_constants import DEFAULT_PICTURE_LOCATION


class User(AbstractUser):
    is_stylist = models.CharField(max_length=3, default="NO")
    profile_picture = models.FileField(upload_to='profile_pictures/%Y/%m/%d', null=True, blank=True,
                                       default=DEFAULT_PICTURE_LOCATION)
    biography = models.TextField(blank=True)
    location = models.TextField(blank=True)
    hair_type = models.TextField(blank=True)
    hidden_hair_type = models.TextField(blank=True)


class Menu(models.Model):
    name = models.CharField(max_length=20)
    category = models.TextField(default='MAIN')
    # Might get rid of price.
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    picture = models.FileField(upload_to='menu/%Y/%m/%d', null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Category: " + self.category + " || Option: " + self.name


class ItemInBill(models.Model):
    item_portfolio = models.ForeignKey('stylist.PortfolioHaircut', related_name='item_portfolio', null=True, blank=True)
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

    #this field should be removed because customer's can choose more than one possible option.
    haircut = models.ForeignKey('stylist.PortfolioHaircut', null=True, blank=True)

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

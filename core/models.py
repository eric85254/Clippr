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
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    picture = models.FileField(upload_to='menu/%Y/%m/%d', null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Category: " + self.category + " || Option: " + self.name


class Bill(models.Model):
    item_menu = models.ForeignKey('core.Menu', related_name='item_menu', null=True, blank=True)
    item_portfolio = models.ForeignKey('stylist.PortfolioHaircut', related_name='item_portfolio', null=True, blank=True)
    item_custom = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    appointment = models.ForeignKey('core.Appointment', on_delete=models.SET_NULL, null=True)


class Review(models.Model):
    reviewer = models.ForeignKey('core.User', related_name='reviewer', on_delete=models.SET_NULL, null=True)
    reviewee = models.ForeignKey('core.User', related_name='reviewee', on_delete=models.SET_NULL, null=True)
    appointment = models.ForeignKey('core.Appointment', related_name='appointment', on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField()


class Appointment(models.Model):
    # Changed it so that record of appointment can't be deleted if any user is deleted.
    # ^ removed on_delete=models.CASCADE. double check to make sure this works.
    stylist = models.ForeignKey('core.User', related_name='stylist', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey('core.User', related_name='customer', on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now)
    price = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    haircut = models.ForeignKey('stylist.PortfolioHaircut', null=True, blank=True)


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
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Get rid of both Stylist and Customer models and just have simple User model with validation
#  to whether or not they're a stylist?
class Stylist(models.Model):

	# Basic Information
	stylist_picture = models.FileField(upload_to='stylist/%Y/%m/%d', null=True, blank=True)
	biography = models.CharField(max_length=500, blank=True)

	# Stylist Specific Information
	location = models.CharField(max_length=500, blank=True)


# Change price_modifier field name to price
class Deals(models.Model):
	stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
	description = models.CharField(max_length=500)
	price_modifier = models.DecimalField


# Add another field to Haircut model that stores Customer?
# Then you can look at customer haircut history and add the haircut you've done to the history
class Haircut(models.Model):
	haircut_stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
	haircut_picture = models.FileField(upload_to='haircuts/%Y/%m/%d', null=True, blank=True)
	haircut_name = models.CharField(max_length=30)
	haircut_description = models.CharField(max_length=500)


class Appointments(models.Model):
	stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
	customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
	location = models.CharField(max_length=500)
	date = models.DateTimeField(default=datetime.now)
	price = models.DecimalField
	haircut = models.ForeignKey(Haircut)


class User(AbstractUser):
	is_stylist = models.CharField(max_length=3, default="NO")
	stylist = models.OneToOneField(Stylist, null=True, blank=True)
	customer = models.OneToOneField('customer.Customer', null=True, blank=True)
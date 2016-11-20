from django.contrib.auth.models import AbstractUser
from django.db import models


class Stylist(models.Model):

	# Basic Information
	name = models.CharField(max_length=20)
	email = models.EmailField()
	stylist_picture = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)

	# Stylist Specific Information
	price = models.DecimalField
		# Instead of having a ratings field, just calculate it from customer reviews?
	location = models.CharField(max_length=500)


class Deals(models.Model):
	stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
	description = models.CharField(max_length=500)
	price_modifier = models.DecimalField


class Haircut(models.Model):
	haircut_stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
	haircut_picture = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)
	haircut_name = models.CharField(max_length=30)
	haircut_description = models.CharField(max_length=500)


class Appointments(models.Model):
	stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
	customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
	location = models.CharField(max_length=500)
	date = models.DateTimeField
	price = models.DecimalField
	haircut = models.ForeignKey(Haircut)


class User(AbstractUser):
	is_stylist = models.CharField(max_length=3, default="NO")
	stylist = models.OneToOneField(Stylist, null=True, blank=True)
	customer = models.OneToOneField('customer.Customer', null=True, blank=True)
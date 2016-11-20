from django.contrib.auth.models import User, AbstractUser
from django.db import models

class Stylist(models.Model):

	# Basic Information
	name = models.CharField(max_length=20)
	email = models.EmailField()
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	stylist_picture = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)

	# Stylist Specific Information
	price = models.DecimalField
	haircuts = models.ManyToManyField(Haircuts)
		# Instead of having a ratings field, just calculate it from customer reviews?
	location = models.CharField(max_length=500)


class Deals(models.Model):
	stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
	description = models.CharField(max_length=500)
	price_modifier = models.DecimalField


class Haircuts(models.Model):
	haircut_picture = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)
	haircut_name = models.CharField(max_length=30)
	haircut_description = models.CharField(max_length=500)


class Appointments(models.Model):
	stylist = models.ForeignKey(Stylist, on_delete=models.CASCADE)
	# customer = foreign key


class CustomUser(AbstractUser):
	is_stylist = models.BooleanField
	stylist = models.OneToOneField(Stylist, null=True, blank=True)
	# customer
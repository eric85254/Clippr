from django.db import models


class Customer(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()
	customer_picture = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)


class Reviews(models.Model):
	stylist = models.ForeignKey('stylist.Stylist', on_delete=models.CASCADE)
	rating = models.DecimalField
	description = models.CharField(max_length=500)


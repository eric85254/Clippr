from django.db import models


class Reviews(models.Model):
	stylist = models.ForeignKey('core.User', on_delete=models.CASCADE)
	rating = models.DecimalField
	description = models.CharField(max_length=500)

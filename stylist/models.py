from datetime import datetime as datetime
from django.db import models


# Change price_modifier field name to price
class Deal(models.Model):
    stylist = models.ForeignKey('core.User', on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    price_modifier = models.DecimalField


# Add another field to Haircut model that stores Customer?
# Then you can look at customer haircut history and add the haircut you've done to the history
class Haircut(models.Model):
    haircut_stylist = models.ForeignKey('core.User', on_delete=models.CASCADE)
    haircut_picture = models.FileField(upload_to='haircuts/%Y/%m/%d', null=True, blank=True)
    haircut_name = models.CharField(max_length=30)
    haircut_description = models.CharField(max_length=500)


class Appointment(models.Model):
    stylist = models.ForeignKey('core.User', related_name='stylist', on_delete=models.CASCADE)
    customer = models.ForeignKey('core.User', related_name='customer', on_delete=models.CASCADE)
    location = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now)
    price = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    haircut = models.ForeignKey(Haircut, null=True, blank=True)


class Application(models.Model):
    applicant = models.ForeignKey('core.User', on_delete=models.CASCADE)
    application_status = models.CharField(max_length=20, default='PENDING')
    denied_reason = models.CharField(max_length=1000, blank=True)
    reason = models.CharField(max_length=1000)
    interview_time = models.DateTimeField(null=True, blank=True)
    # ToDo: Figure out what fields we want for a stylist application

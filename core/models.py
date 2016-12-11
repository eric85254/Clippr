from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
	is_stylist = models.CharField(max_length=3, default="NO")

	profile_picture = models.FileField(upload_to='profile_pictures/%Y/%m/%d', null=True, blank=True)
	biography = models.CharField(max_length=500, blank=True)

	location = models.CharField(max_length=500, blank=True)
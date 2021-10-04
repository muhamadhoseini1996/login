from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=250)
    # user = models.CharField(max_length=10)
    # password = models.CharField(max_length=12)
    # age = models.CharField(max_length=3)


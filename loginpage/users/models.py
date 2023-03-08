from django.db import models
# Create your models here.


class Details(models.Model):
    username = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=128)
    password_confirmation = models.CharField(max_length=128)
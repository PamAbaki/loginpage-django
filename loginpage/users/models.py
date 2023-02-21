from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()

class Profile(models.Model):
    username = models.CharField(max_length=80)
    password1 = models.CharField(max_length=80)
    password2 = models.CharField(max_length=80)

def _str_(self):
    return self.user.username
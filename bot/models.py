from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
# Create your models here.

"""
class TelegramUsers(AbstractUser) :
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, null=True, unique=True)
    password = models.CharField(max_length=255, null=True)
    is_bot = models.BooleanField(default=False)
    email = models.CharField(max_length=255, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['user_id','first_name','last_name']
    
    def save(self, *args, **kwargs):
        username = str(self.first_name) + str(self.user_id)
        super(TelegramUsers, self).save(*args, **kwargs)
    
    def __str__(self) :
        return self.first_name
        
"""

class TelegramUsers(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    is_bot = models.BooleanField(default=False)
    email = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"{self.user_id}_{self.last_name}"
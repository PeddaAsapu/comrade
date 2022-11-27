from enum import unique
from django.db import models
from django.contrib.auth import get_user_model
from bot.models import *
# Create your models here.

class ModeOfTransport(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    
    def __str__(self) :
        return self.name

class TransportProvider(models.Model) :
    # qantas, IRCTC, Singapore Airlines
    name = models.CharField(max_length=50, unique=True)
    
    
    def __str__(self) :
        return self.name


class VehicleDetail(models.Model):
    name = models.CharField(max_length=255)
    provider = models.ForeignKey(TransportProvider, on_delete=models.PROTECT)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self) :
        return self.name


class Trip(models.Model):
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    user = models.ForeignKey(TelegramUsers, on_delete=models.PROTECT)
    mode_of_transport = models.ForeignKey(ModeOfTransport, on_delete=models.PROTECT)
    vehicle = models.ForeignKey(VehicleDetail, on_delete=models.CASCADE, null=True)
    travel_date_time = models.DateTimeField()
    
    #can move this to another model later - if needed 
    source_location = models.CharField(max_length=255, null=False)
    destination_location = models.CharField(max_length=255, null=False)
    
    
    def __str__(self) :
        return f"{self.user.first_name}_{self.vehicle.code}_{self.travel_date_time.date()}"
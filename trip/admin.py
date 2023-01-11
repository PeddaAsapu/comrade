from django.contrib import admin
from .models import *
# Register your models here.

class TripAdmin(admin.ModelAdmin):
    list_display = ['user', 'source_location',  'destination_location']

admin.site.register(ModeOfTransport)
admin.site.register(TransportProvider)
admin.site.register(VehicleDetail)
admin.site.register(Trip, TripAdmin)
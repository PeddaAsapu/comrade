from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ModeOfTransport)
admin.site.register(TransportProvider)
admin.site.register(VehicleDetail)
admin.site.register(Trip)
from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'first_name',  'last_name']

# Register your models here.
admin.site.register(TelegramUsers, UsersAdmin)
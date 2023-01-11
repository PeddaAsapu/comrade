from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def testviewset(request):
    print("request : ", request)
    return HttpResponse('Ok')

def trip_details(request) :
    trip_details = Trip.objects.all()
    
    return HttpResponse(trip_details)
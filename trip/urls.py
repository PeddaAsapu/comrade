from django.urls import path
from . import views

urlpatterns = [
    path('test', views.testviewset, name='test'),
    path('details', views.trip_details, name='trip_details')
]
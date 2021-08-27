from django import urls
from django.urls import path 
from .views import *


app_name='crud'

urlpatterns = [
    path('',Autoclass.as_view(),name='Autoclass'),
    path('delete/<int:pk>/',DeleteAula,name="DeleteAula" ),
    path('add/',NovaAula.as_view(),name='NovaAula'),
    path('adcionar',AddAula,name='adcionar')
]


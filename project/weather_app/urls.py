from django.urls import path
from .views import *

urlpatterns = [
    path('w/', get_weather_data, name='get_weather_data'),
]

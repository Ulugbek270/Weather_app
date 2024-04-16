from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
import urllib.request
from django.conf import settings  # Ensure you import settings this way

from project import settings


def get_weather_data(request):
    print(1)
    if request.method == 'POST':
        print(2)

        city = request.POST.get('city')
        print(3)

        # to get data Api

        # OPENWEATHERMAP_API_KEY = '1cd63f42c20da919b414b64b6467b639'
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=1cd63f42c20da919b414b64b6467b639').read()
        print(4)

        # 1cd63f42c20da919b414b64b6467b639
        # cd4415a99345841edbb9040348e3f2d6

        convert = json.loads(source)
        print(5)

        dict_weather = {
            'country_code': str(convert['sys']['country']),
            'coord': str(convert["coord"]["lon"]) + " " + str(convert["coord"]["lat"]),
            'temp': str(convert["main"]['temp']),
            'pressure': str(convert['main']["pressure"]),
            'humidity': str(convert['main']['humidity']),
            'main': str(convert["weather"][0]['main']),
            'description': str(convert["weather"][0]['description']),
            'icon': convert["weather"][0]['icon'],
            'city': city}
        print(6)

    else:
        dict_weather = {}
        print(7)

    return render(request, 'base.html', dict_weather)

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
import urllib.request
from datetime import date


def get_weather_data(request):

    # Get the current date
    current_date = date.today()


    format5 = current_date.strftime("%A, %B %d, %Y")
    date_lst = format5.split()

    weekday = date_lst[0]
    month = date_lst[1]
    day = date_lst[2]
    year = date_lst[3]

    if request.method == 'POST':
        city = request.POST.get('city')
        dict_weather = {}

        try:
            # to get data Api
            source = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=1cd63f42c20da919b414b64b6467b639').read()
            print(source)

            # cd4415a99345841edbb9040348e3f2d6

            convert = json.loads(source)

            dict_weather = {
                'country_code': str(convert['sys']['country']),
                'coord': str(convert["coord"]["lon"]) + " " + str(convert["coord"]["lat"]),

                'temp': int(convert["main"]['temp']),

                'pressure': str(convert['main']["pressure"]),
                'speed': str(convert["wind"]['speed']),
                'humidity': str(convert['main']['humidity']),
                'main': str(convert["weather"][0]['main']),
                'description': str(convert["weather"][0]['description']),
                'icon': convert["weather"][0]['icon'],
                'city': city}

            context = {"city": city,
                       "dict_weather": dict_weather,
                       'weakday': weekday,
                       'month': month,
                       'day': day,
                       'year': year,
                       # 'temp_int': int(dict_weather.temp),

                       }
            return render(request, 'base.html', context)
        except Exception as e:
            print(e)



    else:
        dict_weather = {}

        return render(request, 'base.html', dict_weather)

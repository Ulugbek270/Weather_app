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
        dict_weather_td = {}
        # dict_weather_tm = {}

        try:
            # to get data Api
            source_today = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=1cd63f42c20da919b414b64b6467b639').read()

            # source_tommorow = urllib.request.urlopen(
            #     'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&units=metric&appid=1cd63f42c20da919b414b64b6467b639').read()

            convert_td = json.loads(source_today)
            # convert_tm = json.loads(source_tommorow)

            dict_weather_td = {
                'country_code': str(convert_td['sys']['country']),
                'coord': str(convert_td["coord"]["lon"]) + " " + str(convert_td["coord"]["lat"]),
                'temp': int(convert_td["main"]['temp']),
                'pressure': str(convert_td['main']["pressure"]),
                'speed': str(convert_td["wind"]['speed']),
                'humidity': str(convert_td['main']['humidity']),
                'main': str(convert_td["weather"][0]['main']),
                'description': str(convert_td["weather"][0]['description']),
                'icon': convert_td["weather"][0]['icon'],
                'city': city}

            # next_day_weather = convert_tm['list'][0]
            # dict_weather_tm = {
            #     'temp': int(next_day_weather["main"]['temp']),

            # }

            context = {"city": city,
                       "dict_weather_td": dict_weather_td,
                       # "dict_weather_tm": dict_weather_tm,
                       'weakday': weekday,
                       'month': month,
                       'day': day,
                       'year': year,

                       }
            return render(request, 'base.html', context)
        except Exception as e:
            print(e)



    else:
        dict_weather = {}

        return render(request, 'base.html', dict_weather)

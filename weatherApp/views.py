from django.shortcuts import render

import urllib.request
import json

# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        try:
            source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='
                                      +city+'&units=metric&appid=4078c4084022206cf7a937c2a2e62ab6').read()
            listOfData = json.loads(source)
            data = {
                "country_code": str(listOfData["sys"]["country"]),
                "coordinate": str(listOfData["coord"]["lon"]) + ' ,' + str(listOfData['coord']['lat']),
                "temp": str(listOfData['main']['temp']) + ' °C',
                "pressure": str(listOfData['main']['pressure']),
                "humidity": str(listOfData['main']['humidity']),
                "main": str(listOfData['weather'][0]['main']),
                "description": str(listOfData['weather'][0]['description']),
                "icon": str(listOfData['weather'][0]['icon']),
                "cityname": str(city).capitalize()
            }
        except:
            data={"error":"Country Not Found"}
        finally:
            return render(request, 'main/index.html', data)
    else:
        data={}
    return render(request,'main/index.html',data)

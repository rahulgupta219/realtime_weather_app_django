from django.http.response import HttpResponse
from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=f46c53d22d856453b5eb85918b1127d1').read()
        json_data = json.loads(res)
        data={
            "country_code": (str(json_data['sys']['country'])),
            "coordinate": str(json_data['coord']['lon'])+' Long ' + str(json_data['coord']['lat'])+" Lat",
            "temperature": str(round((json_data['main']['temp']-273.15),2)) +' °C',
            "pressure": str(json_data['main']['pressure'])+" hPA",
            "humidity": str(json_data['main']['humidity']) + " %",
            "city":str(city).upper(),
        }
    else:
        data={}   
    return render(request,'index.html',data)
from django.shortcuts import render,redirect
from .models import Pollution
import requests

from django.contrib import messages
import urllib.request
# Create your views here.

def home(request):
    cities=Pollution.objects.all().order_by('-date')[:5]
    
    
    context={'all_city' :cities,
    'ac':'home'}

    
    return render(request,'pollution/home.html',context)


    
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=34d2e4dab4effca1d30844dcd273f2ef'

    # source = urllib.request.urlopen( 
    #         'http://api.openweathermap.org/data/2.5/weather?q =' 
    #                 + city + '&appid = your_api_key_here').read()
    # cities =City.objects.all()

    # for city in cities:
                
    #     r = requests.get(url.format(city)).json()
    #     
    # #     city_weather = {
    #         'city': city.name,
    #         'temperature': r['main']['temp'],
    #         'description': r['weather'][0]['description'],
    #         'icon': r['weather'][0]['icon'],
    #     }
    # # #context={'all_city':city_weather}
    


def addCity(request):
    
    if request.method=="POST":
        city=request.POST['content']
        
        url='https://api.waqi.info/feed/{}/?token=8d006b81423b8a95ac3e73caa6c4ba2407852103'
        poll=requests.get(url.format(city)).json()
        city=city.lower()
        city=city.capitalize()
        
        if not Pollution.objects.filter(name=city).exists():
                
            city_add=Pollution(name=city)
            if poll["status"]=="ok":
                city_add.save()
            else:
                messages.error(request,'Please enter a valid city')
                return redirect('/pollution')
        
       
        

        if poll["status"]=="ok":
                
            
            city_pollution = {
                
                'city': city,
                'aqi':poll['data']['aqi'],
                'time':poll['data']['time']['s'],
                'pm25':poll['data']['iaqi']['pm25']['v'],
            }
            
            
            return render(request,'pollution/pollution.html',city_pollution)
        else:
            messages.error(request,'Please enter a valid city')
            return redirect('/pollution')


    else:
        messages.error(request,'Please do a post request')
        return redirect('/pollution')


def from_list(request,slug):
    Cit=Pollution.objects.get(id=slug)
    city=Cit.name
    url = 'https://api.waqi.info/feed/{}/?token=8d006b81423b8a95ac3e73caa6c4ba2407852103'
    poll = requests.get(url.format(city)).json()
    if poll["status"]=="ok":
        
        city_pollution = {
                
                'city': city,
                'aqi':poll['data']['aqi'],
                'time':poll['data']['time']['s'],
                'pm25':poll['data']['iaqi']['pm25']['v'],
        }
        

    return render(request,'pollution/pollution.html',city_pollution)

def delete(request,slug):
    Pollution.objects.filter(id=slug).delete()
    return redirect('/pollution')

def currentCity(request):
    
    if request.method=="POST":

        res = requests.get('https://ipinfo.io/')
        data = res.json()
        city = data['city']

        city=city.lower()
        city=city.capitalize()

        url='https://api.waqi.info/feed/{}/?token=8d006b81423b8a95ac3e73caa6c4ba2407852103'
        poll=requests.get(url.format(city)).json()

        if not Pollution.objects.filter(name=city).exists():
                
            city_add=Pollution(name=city)
            if poll["status"]=="ok":
                city_add.save()
            else:
                messages.error(request,'Please enter a valid city')
                return redirect('/pollution')
        
       
        

        if poll["status"]=="ok":
            
          
            city=city.capitalize()
            city_pollution = {
                
                'city': city,
                'aqi':poll['data']['aqi'],
                'time':poll['data']['time']['s'],
                'pm25':poll['data']['iaqi']['pm25']['v'],
        }
            return render(request,'pollution/pollution.html',city_pollution)
        else:
            messages.error(request,'Please enter a valid city')
            return redirect('/pollution')


    else:
        messages.error(request,'Please do a post request')
        return redirect('/pollution')


    

    

    
  
        
    
    
from django.shortcuts import render,redirect
from .models import City
import requests

from django.contrib import messages
import urllib.request
# Create your views here.

def home(request):
    cities=City.objects.all().order_by('-date')[:5]
    context={'all_city' :cities}

    
    return render(request,'weather/home.html',context)


    
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
        city=city.lower()
        city=city.capitalize()
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=34d2e4dab4effca1d30844dcd273f2ef'
        r = requests.get(url.format(city)).json()
        if r["cod"]!="404" and r['cod']!="200":
            if not City.objects.filter(name=city).exists():
                
                city_add=City(name=city)
                if r["cod"]!="404" and r['cod']!="200":
                    
                    city_add.save()
                else:
                    messages.error(request,'Please enter a valid city')
                    return redirect('/weather')
            
       
        

        if r["cod"]!="404":
            
            city=city.capitalize()
            city_weather = {
                
                'city': city,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                'pressure':r['main']['pressure'],
                'humidity':r['main']['humidity'],
                'min_temp':r['main']['temp_min'],
                'max_temp':r['main']['temp_max'],
                'country':r['sys']['country'],
            }
            
            url='https://api.waqi.info/feed/{}/?token=8d006b81423b8a95ac3e73caa6c4ba2407852103'
            poll=requests.get(url.format(city)).json()
        
            return render(request,'weather/weather.html',city_weather)
        else:
            messages.error(request,'Please enter a valid city')
            return redirect('/weather')


    else:
        messages.error(request,'Please do a post request')
        return redirect('/weather')


def currentCity(request):
    
    if request.method=="POST":

        res = requests.get('https://ipinfo.io/')
        data = res.json()

        city = data['city']
        city=city.lower()
        city=city.capitalize()
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=34d2e4dab4effca1d30844dcd273f2ef'
        r = requests.get(url.format(city)).json()
        if not City.objects.filter(name=city).exists():
            
            city_add=City(name=city)
            if r["cod"]!="404":
                city_add.save()
            else:
                messages.error(request,'Please enter a valid city')
                return redirect('/weather')
        
       
        

        if r["cod"]!="404":
            
            city_weather = {
                
                'city': city,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                'pressure':r['main']['pressure'],
                'humidity':r['main']['humidity'],
                'min_temp':r['main']['temp_min'],
                'max_temp':r['main']['temp_max'],
                'country':r['sys']['country'],
            }
            
            url='https://api.waqi.info/feed/{}/?token=8d006b81423b8a95ac3e73caa6c4ba2407852103'
            poll=requests.get(url.format(city)).json()
            
            return render(request,'weather/weather.html',city_weather)
        else:
            messages.error(request,'Please enter a valid city')
            return redirect('/weather')


    else:
        messages.error(request,'Please do a post request')
        return redirect('/weather')


def from_list(request,slug):
    Cit=City.objects.get(id=slug)
    city=Cit.name
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=34d2e4dab4effca1d30844dcd273f2ef'
    r = requests.get(url.format(city)).json()
    if r["cod"]!="404":
                
        city_weather = {
                
                'city': city,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
                'pressure':r['main']['pressure'],
                'humidity':r['main']['humidity'],
                'min_temp':r['main']['temp_min'],
                'max_temp':r['main']['temp_max'],
                'country':r['sys']['country'],
        }
    return render(request,'weather/weather.html',city_weather)

def delete(request,slug):
    City.objects.filter(id=slug).delete()
    return redirect('/weather')

        
    

    

    
  
        
    
    
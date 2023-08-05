from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests
from django.contrib import messages


# Create your views here.

def homepage(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)






def home(request):
    if 'city' in request.POST:
         city = request.POST['city']
    else:
         city = None     
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=95c9c6eab7ea5475d073649ff78be209'
    PARAMS = {'units':'metric'}
    
    try:
          data = requests.get(url,params=PARAMS).json()
          description = data['weather'][0]['description']
          icon = data['weather'][0]['icon']
          temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'weatherapp/index.html' , {'description':description , 'icon':icon ,'temp':temp , 'day':day , 'city':city, 'exception_occurred':False })
    
    except KeyError:
          messages.error(request,'Entered data is not available to API')   
          # city = 'indore'
          # data = requests.get(url,params=PARAMS).json()
          
          # description = data['weather'][0]['description']
          # icon = data['weather'][0]['icon']
          # temp = data['main']['temp']
          day = datetime.date.today()

          return render(request,'weatherapp/index.html' ,{'description':'clear sky', 'icon':'01d'  ,'temp':25 , 'day':day , 'city':'indore' , 'exception_occurred':True })
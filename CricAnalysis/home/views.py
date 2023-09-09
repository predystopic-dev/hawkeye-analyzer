from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests
from django.contrib import messages
# from home.models import Team

# Create your views here.

def homepage(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


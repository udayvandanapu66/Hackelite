from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def index(request):#Defining a function and rendering it using http response for index page.
    return render(request, 'dashboard/index.html')

def home(request):##Defining a function and rendering it using http response for home page.
    return render(request, 'dashboard/home.html')

def about(request):#Defining a function and rendering it using http response for about page.
    return render(request, 'dashboard/about.html')
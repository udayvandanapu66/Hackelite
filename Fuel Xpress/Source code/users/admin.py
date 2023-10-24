from django.contrib import admin #Import the admin module from django.contrib
from .models import Profile #Import the Profile model from the .models module

admin.site.register(Profile) #Register the Profile model with the admin site

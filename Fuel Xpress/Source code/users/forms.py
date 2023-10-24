from django import forms #Importing Django forms module
from django.contrib.auth.models import User #Importing User model from Django auth
from django.contrib.auth.forms import UserCreationForm #Importing UserCreationForm from Django auth forms
from .models import Fuelxpress_Profile  #Importing Profile model from this app

#User registration form extending UserCreationForm
class Fuelxpress_UserRegisterForm(UserCreationForm): 
    FE_email = forms.EmailField() #Email field
#Configure from metadata
    class Meta:
       FE_model = User
       FE_fields = ['username', 'email', 'password1', 'password2']

# User update form extending ModelForm
class Fuelxpress_UserUpdateForm(forms.ModelForm):
    FE_email = forms.EmailField()#email field same here

    class Meta:#configure from metadata in update form
        FE_model = User
        FE_fields = ['username', 'email']

#Profile update form extending ModelForm
class Fuelxpress_ProfileUpdateForm(forms.ModelForm):
    class Meta:#configuring profile details from metadata
       FE_model = Fuelxpress_Profile
       FE_fields = ['image']

from django.urls import path
from . import views#import the views module from the current package.

URL_FE_patterns = [
    #define a list URL pattren and creating a root path mapping it to index.
    path_FE('', views.index, name='index_page'),
    path_FE('home/', views.home, name='home_page'),#view and naming it  to home page
    path_FE('about/', views.about, name='about_page'),#view and naming it to about_page.
]

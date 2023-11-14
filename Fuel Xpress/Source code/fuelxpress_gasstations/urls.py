from django.urls import path
from . import views

urlpatterns = [
    path('gasstations/', views.fuelxpress_gas_station_list, name='fuelxpress_gas_station_list'),
    path('gasstations/<int:gas_station_id>/', views.fuelxpress_gas_station_detail, name='fuelxpress_gas_station_detail'),
]

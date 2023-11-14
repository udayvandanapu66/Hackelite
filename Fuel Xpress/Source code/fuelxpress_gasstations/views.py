#Impoting the necessary modules from django
from django.shortcuts import render, get_object_or_404
from .models import FuelXpressGasStation
# View function for listing all FuelXpress gas stations
def fuelxpress_gas_station_list(request):
    gas_stations = FuelXpressGasStation.objects.all()
    return render(request, 'fuelxpress_gasstations/fuelxpress_gas_station_list.html', {'gas_stations': gas_stations})
# View function for displaying details of a specific FuelXpress gas station
def fuelxpress_gas_station_detail(request, gas_station_id):
    gas_station = get_object_or_404(FuelXpressGasStation, pk=gas_station_id)
    return render(request, 'fuelxpress_gasstations/fuelxpress_gas_station_detail.html', {'gas_station': gas_station})

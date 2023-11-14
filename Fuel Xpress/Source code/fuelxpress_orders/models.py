#importing the required modules from django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from fuelxpress_gasstations.models import FuelXpressGasStation
from fuelxpress_drivers.models import FuelXpressDriver
from django.urls import reverse

#Defining the FuelXpressorder model
class FuelXpressOrder(models.Model):
    FX_user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Defining the foreign key relationship
    FX_gas_station = models.ForeignKey(FuelXpressGasStation, on_delete=models.CASCADE)  
    FX_driver = models.ForeignKey(FuelXpressDriver, on_delete=models.CASCADE) 
    #Definig the character field 
    FX_fuel_type = models.CharField(max_length=100)
    FX_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    FX_delivery_location = models.TextField()
    FX_order_status = models.CharField(max_length=50, default="Pending")
    #Defining the date-time field to store
    FX_order_date = models.DateTimeField(default=timezone.now) 
#Definig the human-redable string representation
    def __str__(self):
        return f"Order for {self.FX_user.username}"

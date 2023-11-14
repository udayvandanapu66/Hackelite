from django.db import models

class FuelXpressGasStation(models.Model):
    FX_name = models.CharField(max_length=100)
    FX_phone_number = models.CharField(max_length=100)
    FX_email = models.EmailField()
    FX_location = models.CharField(max_length=200)
    FX_inventory = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.FX_name

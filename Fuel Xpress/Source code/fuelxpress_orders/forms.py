from django import forms
from .models import FuelXpressOrder

class FuelXpressOrderForm(forms.ModelForm):#here i declare the class name as FuelXpressOrderForm.
    class Meta:
        #specifying the model that is associated with this form
        model = FuelXpressOrder
        fields = ['FX_fuel_type','FX_gas_station', 'FX_driver', 'FX_quantity', 'FX_delivery_location']  # Specify the fields required in the form

    def __init__(self, *args, **kwargs):
        #Calling the parent class constructor and updating the attributes of Fuelxpress
        super(FuelXpressOrderForm, self).__init__(*args, **kwargs)
        self.fields['FX_fuel_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['FX_quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['FX_delivery_location'].widget.attrs.update({'class': 'form-control'})

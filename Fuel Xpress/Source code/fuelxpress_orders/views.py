#Importing the necessary modules
from django.shortcuts import render, redirect
from .forms import FuelXpressOrderForm
from django.shortcuts import get_object_or_404
from .models import FuelXpressOrder
from django.contrib.auth.decorators import login_required

@login_required
def fuelxpress_create_order(request):#here we create function named as fuelxpress_create_order.
    if request.method == 'POST':
        form = FuelXpressOrderForm(request.POST)
        if form.is_valid():
            fuelxpress_order = form.save(commit=False)
            fuelxpress_order.FX_user = request.user  # Set the user associated with the order
            fuelxpress_order.save()
            return redirect('fuelxpress_order_detail', order_id=fuelxpress_order.pk)
    else:
        form = FuelXpressOrderForm()
    return render(request, 'fuelxpress_orders/fuelxpress_order_create.html', {'form': form})

@login_required
def fuelxpress_order_detail(request, order_id):#here we create function named as fuelxpress_order_detail.
    order = get_object_or_404(FuelXpressOrder, pk=order_id)
    return render(request, 'fuelxpress_orders/fuelxpress_order_detail.html', {'order': order})

@login_required 
def fuelxpress_order_list(request):#here we create function named as fuelxpress_order_list.
    orders = FuelXpressOrder.objects.filter(FX_user=request.user)  # Use the correct field name here
    return render(request, 'fuelxpress_orders/fuelxpress_order_list.html', {'orders': orders})
from django.urls import path
from . import views

# urlpatterns for FuelXpress orders
urlpatterns = [
    #urlpatterns for creating a new order
    path('create/', views.fuelxpress_create_order, name='fuelxpress_create_order'),
    # urlpatterns for viewing details of a specific order
    path('<int:order_id>/', views.fuelxpress_order_detail, name='fuelxpress_order_detail'),
    # urlpatterns for listing all orders
    path('list/', views.fuelxpress_order_list, name='fuelxpress_order_list'),
]

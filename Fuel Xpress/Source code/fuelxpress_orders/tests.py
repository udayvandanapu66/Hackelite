from django.test import TestCase  # importing library for test case.
from .models import FuelXpressOrder 
from django.contrib.auth.models import User
from fuelxpress_gasstations.models import FuelXpressGasStation
from fuelxpress_drivers.models import FuelXpressDriver
from django.utils import timezone

class OrderTestCase(TestCase):
    def setUp(self):
        # Create a sample user
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        # Create a sample GasStation with inventory
        self.gas_station = FuelXpressGasStation.objects.create(
            FX_name="Test Gas Station",
            FX_phone_number="123-456-7890",
            FX_email="test@example.com",
            FX_location="123 Test Street",
            FX_inventory=1000.00,
        )

        # Create a sample Driver
        self.driver = FuelXpressDriver.objects.create(FX_name="Test Driver", FX_license_number="12345")

        # Create a sample Order instance for testing
        self.order = FuelXpressOrder(
            FX_user=self.user,
            FX_gas_station=self.gas_station,
            FX_driver=self.driver,
            FX_fuel_type="Regular",
            FX_quantity=10.5,
            FX_delivery_location="123 Test Street",
            FX_order_status="Pending",
            FX_order_date=timezone.now(),
        )
        self.order.save()
  # here we define different types of functions for user,gas station ,order driver and order fuel type.
    def test_order_user(self):
        order = FuelXpressOrder.objects.get(FX_fuel_type="Regular")
        self.assertEqual(order.FX_user, self.user)

    def test_order_gas_station(self):
        order = FuelXpressOrder.objects.get(FX_fuel_type="Regular")
        self.assertEqual(order.FX_gas_station, self.gas_station)

    def test_order_driver(self):
        order = FuelXpressOrder.objects.get(FX_fuel_type="Regular")
        self.assertEqual(order.FX_driver, self.driver)

    def test_order_fuel_type(self):
        order = FuelXpressOrder.objects.get(FX_fuel_type="Regular")
        self.assertEqual(order.FX_fuel_type, "Regular")

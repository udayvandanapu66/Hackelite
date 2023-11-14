from django.test import TestCase
from .models import FuelXpressGasStation

class GasStationTestCase(TestCase):
    def setUp(self):
        # Create a sample GasStation instance for testing
        self.gas_station = FuelXpressGasStation(
            FX_name="Test Gas Station",
            FX_phone_number="123-456-7890",
            FX_email="test@example.com",
            FX_location="123 Test Street",
            FX_inventory=1000.00,
        )
        self.gas_station.save()

    def test_gas_station_name(self):
        # Retrieve the gas station from the database
        gas_station = FuelXpressGasStation.objects.get(FX_name="Test Gas Station")
        self.assertEqual(gas_station.FX_name, "Test Gas Station")

    def test_gas_station_inventory(self):
        gas_station = FuelXpressGasStation.objects.get(FX_name="Test Gas Station")
        self.assertEqual(gas_station.FX_inventory, 1000.00)

    def test_gas_station_email(self):
        gas_station = FuelXpressGasStation.objects.get(FX_name="Test Gas Station")
        self.assertEqual(gas_station.FX_email, "test@example.com")

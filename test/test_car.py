import unittest
from datetime import datetime
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery
from tires.carriganTires import CarriganTires
from tires.octoprimeTires import OctoprimeTires


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())


class TestWillobyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(last_service_date=last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(last_service_date=last_service_date)
        self.assertFalse(battery.needs_service())


class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        sensor_data = [0.2, 0.3, 0.4, 0.9]
        tires = CarriganTires(sensor_data)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        sensor_data = [0.1, 0.2, 0.3, 0.4]
        tires = CarriganTires(sensor_data)
        self.assertFalse(tires.needs_service())


class TestOctorimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        sensor_data = [0.7, 0.7, 0.8, 0.8]
        tires = OctoprimeTires(sensor_data)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        sensor_data = [0.7, 0.5, 0.8, 0.7]
        tires = OctoprimeTires(sensor_data)
        self.assertFalse(tires.needs_service())


# run the tests
if __name__ == '__main__':
    unittest.main()

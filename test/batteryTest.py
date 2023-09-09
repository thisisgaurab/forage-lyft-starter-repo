from battery.battery_type.nubbinBattery import NubbinBattery
from battery.battery_type.spindlerBattery import SpindlerBattery

import datetime
import unittest

class testingNubbinBattery(unittest.TestCase):
    def testing_needs_service_true(self):
        current_date = datetime.datetime(2023, 9, 2)
        last_service_date = datetime.datetime(2015, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def testing_needs_service_false(self):
        current_date = datetime.datetime(2023, 9, 2)
        last_service_date = datetime.datetime(2022, 1, 1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

class testingSpindlerBattery(unittest.TestCase):
    def testing_needs_service_true(self):
        current_date = datetime.datetime(2023, 9, 2)
        last_service_date = datetime.datetime(2019, 1, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def testing_needs_service_false(self):
        current_date = datetime.datetime(2023, 9, 2)
        last_service_date = datetime.datetime(2022, 1, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

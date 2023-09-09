from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

import unittest

class testingCapuletEngine(unittest.TestCase):
    def testing_needs_service_true(self):
        current_mileage = 35000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def testing_needs_service_false(self):
        current_mileage = 55000
        last_service_mileage = 35000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class testingSternmanEngine(unittest.TestCase):
    def testing_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def testing_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

class testingWilloughbyEngine(unittest.TestCase):
    def testing_needs_service_true(self):
        current_mileage = 65000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def testing_needs_service_false(self):
        current_mileage = 80000
        last_service_mileage = 50000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

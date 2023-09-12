import unittest

from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capuletEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capuletEngine.needs_service())

if __name__ == '__main__':
    unittest.main(exit=False)
import unittest

from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughbyEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughbyEngine.needs_service())

if __name__ == '__main__':
    unittest.main(exit=False)
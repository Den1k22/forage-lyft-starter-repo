import unittest

from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        nubbinBattery = SternmanEngine(warning_light_is_on)
        self.assertTrue(nubbinBattery.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        nubbinBattery = nubbinBattery = SternmanEngine(warning_light_is_on)
        self.assertFalse(nubbinBattery.needs_service())

if __name__ == '__main__':
    unittest.main(exit=False)
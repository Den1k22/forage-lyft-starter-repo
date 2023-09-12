import unittest
from datetime import datetime

from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        spindlerBattery = SpindlerBattery(today, last_service_date)
        self.assertTrue(spindlerBattery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        spindlerBattery = SpindlerBattery(today, last_service_date)
        self.assertFalse(spindlerBattery.needs_service())

if __name__ == '__main__':
    unittest.main(exit=False)
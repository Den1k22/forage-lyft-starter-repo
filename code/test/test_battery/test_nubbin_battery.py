import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        nubbinBattery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(nubbinBattery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        nubbinBattery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(nubbinBattery.needs_service())

if __name__ == '__main__':
    unittest.main(exit=False)
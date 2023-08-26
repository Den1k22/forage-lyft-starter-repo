
from car import Car
from capulet_engine import CapuletEngine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine
from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery
from datetime import datetime

class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))
    

carFactory = CarFactory()
print(carFactory.create_calliope(datetime.today().date(), datetime.today().date(), 100, 0))
print(carFactory.create_glissade(datetime.today().date(), datetime.today().date(), 100, 0))
print(carFactory.create_palindrome(datetime.today().date(), datetime.today().date(), False))
print(carFactory.create_rorschach(datetime.today().date(), datetime.today().date(), 100, 0))
print(carFactory.create_thovex(datetime.today().date(), datetime.today().date(), 100, 0))
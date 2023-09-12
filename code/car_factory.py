
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from datetime import datetime

class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(current_date, last_service_date),
            CarriganTires([0,0,0,0]))

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            SpindlerBattery(current_date, last_service_date),
            CarriganTires([0,0,0,0]))

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(
            SternmanEngine(warning_light_on),
            SpindlerBattery(current_date, last_service_date),
            CarriganTires([0,0,0,0]))

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(current_date, last_service_date),
            CarriganTires([0,0,0,0]))

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            NubbinBattery(current_date, last_service_date),
            OctoprimeTires([0,0,0,0]))
    
print(CarFactory.create_calliope(datetime.today().date(), datetime.today().date(), 100, 0))
print(CarFactory.create_glissade(datetime.today().date(), datetime.today().date(), 100, 0))
print(CarFactory.create_palindrome(datetime.today().date(), datetime.today().date(), False))
print(CarFactory.create_rorschach(datetime.today().date(), datetime.today().date(), 100, 0))
print(CarFactory.create_thovex(datetime.today().date(), datetime.today().date(), 100, 0))
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
    
    def __str__(self) -> str:
        return str(self.engine) + str(self.battery) + str(self.needs_service())

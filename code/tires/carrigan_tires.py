from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tires_sensors):
        self.tires_sensors = tires_sensors
        
    def needs_service(self):
        if max(self.tires_sensors) < 0.9:
            return False
        else:
            return True
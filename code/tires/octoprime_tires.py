from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tires_sensors):
        self.tires_sensors = tires_sensors
        
    def needs_service(self):
        if sum(self.tires_sensors) < 3:
            return False
        else:
            return True
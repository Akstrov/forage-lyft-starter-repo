from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, sensor_data):
        self.sensor_data = sensor_data

    def needs_service(self):
        if sum(self.sensor_data) >= 3:
            return True
        return False

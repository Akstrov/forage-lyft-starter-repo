from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, sensor_data):
        self.self_data = sensor_data

    def needs_service(self):
        for i in self.self_data:
            if i >= 0.9:
                return True
        return False

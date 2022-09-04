# check if one class is a subclass of another



class Vehicle:
    def __init__(self):
        self.fuel = 'disel'
    def __str__(self):
        return f'Fuel type: {self.fuel}'
    def move(self):
        print('Vehicle is moving...')

class Bus(Vehicle):
    def job(self):
        print('Public property!')

b = Bus()
print(isinstance(b, Vehicle))
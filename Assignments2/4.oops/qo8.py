# Determine if School_bus is also an instance of the Vehicle class

class Vehicle:
    def __init__(self):
        self.wheels = 4
    def __str__(self):
        return f'No. of wheels: {self.wheels}'
    def move(self):
        return f'Vehicle is moving...'

class Bus(Vehicle):
    def job(self):
        return f'Public transport!'

class School_bus(Bus):
    def job(self):
        return f'Transporting school students...'

sb = School_bus()
print(sb)
print(sb.move())
print(sb.job())
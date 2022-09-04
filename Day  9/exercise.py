# creating class circle

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r * self.r
    def perimeter(self):
        return 2*3.14*self.r
    def __str__(self):
        return f'Radius of the Circle: {self.r}'

radius = float(input('Enter the radius in cm: '))
c = Circle(radius)

print(c)
print('Area of Circle:', c.area(), 'sq.cm')
print('Perimater of Circle: {:.2f} cm'.format(c.perimeter()))

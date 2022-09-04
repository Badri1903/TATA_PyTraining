from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r * self.r

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return 0.5 * self.b * self.h

c = Circle(20)
print('Area of circle: {:.2f} sq.cm'.format(c.area()))

t = Triangle(10, 5)
print('Area of Triangle: {:.2f} sq.cm'.format(t.area()))
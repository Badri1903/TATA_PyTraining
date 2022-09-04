# Area of rectangle

class Rectangle:
    def __init__(self, a, b):
        self.wid=b
        self.len=a
    def area(self):
        return self.len*self.wid

r = Rectangle(10, 20)
print(f'Area of the rectangle: {r.area()}')
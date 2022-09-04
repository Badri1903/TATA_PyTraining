# Create a class Teacher with name, age, and salary attributes, where salary must be a private attribute that cannot be accessed outside the class

class Teacher:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary

rita = Teacher('rita', 28, 25000)
print(rita._Teacher__salary)
print(rita.salary)
# create a child class Teacher that will inherit the properties of Parent class Staff

class Staff:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}'

class Teacher(Staff):
    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}'

rita = Teacher('rita', 25, 28000)
print(rita)
# create a class with instance attributes

class Details:
    def __init__(self, a, b, c, d):
        self.name = a
        self.age = b
        self.weight = c
        self.married = d

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nWeight in kg: {self.weight}\nMarried: {self.married}'

person_1 = Details('Badri', 21, 60.5, False)

print(person_1)



# create a class and using the class instance print all the writable attributes of that object

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Name is {self.name}\nAge is {self.age}'

Player_1 = Player('Dhoni', 30)
print(Player_1)
#                            ......:::::: OOPS ::::::......

############################     STRING OVERLOADING     ###########################
class player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

player_1 = player("Sachin", 35)
print((player_1))
print(str(player_1))
print(player_1.__str__())       # str() == __str__

print('\n'+'-'*40+'\n')


class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Name is {self.name}\nAge is {self.age}'

Player_1 = Player('Dhoni', 30)
print(str(Player_1))
print(Player_1.__str__())
print(Player_1)

print('\n'+'-'*40+'\n')

############################     EQUAL OVERLOADING     ###########################

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f'Name is {self.name}\nSalary is {self.salary}'
    def __eq__(self, other):             # == -> __eq__
        return self.salary == other.salary

emp1 = Employee('Badri', 50000)
print(emp1)
emp2 = Employee('Anju', 50000)
print(emp2)

if emp1 == emp2:
    print(f'{emp1.name}\'s salary is equal to {emp2.name}\'s salary')
else:
    print(f'{emp1.name}\'s salary is not equal to {emp2.name}\'s salary')

print('\n'+'-'*40+'\n')


############################    TOTAL ORDERING    ###########################

# equal is mandatory, overload one more comparison oprtr
from functools import total_ordering

@total_ordering
class Employee:

   def __init__(self, name, salary):
       self.name = name
       self.salary = salary

   def __str__(self):
       return f"Name is {self.name}\nSalary is {self.salary}"

   def __eq__(self, other):                # it work's for not equal to also
       return self.salary == other.salary

   def __gt__(self, other):
       return self.salary > other.salary   # it work's for less than also

emp1 = Employee("Jack", 25000)
print(emp1)

emp2 = Employee("Kurt", 30000)
print(emp2)

print("-" * 40)
if emp1 == emp2:
   print(f"{emp1.name}'s salary {emp1.salary} is NOT equal to {emp2.name}'s salary {emp2.salary} ")
else:
   print(f"{emp1.name}'s salary {emp1.salary} is equal to {emp2.name}'s salary {emp2.salary} ")

if emp1 < emp2:
   print(f"{emp1.name}'s salary {emp1.salary} is less than {emp2.name}'s salary {emp2.salary} ")
else:
   print(f"{emp1.name}'s salary {emp1.salary} is greater than {emp2.name}'s salary {emp2.salary} ")

if emp1 >= emp2:
   print(f"{emp1.name}'s salary {emp1.salary} is less than or equal to {emp2.name}'s salary {emp2.salary} ")
else:
   print(f"{emp1.name}'s salary {emp1.salary} is greater than or equal to {emp2.name}'s salary {emp2.salary} ")


print('\n'+'-'*40+'\n')

############################    ARITHMETIC OPERATORS OVERLOADING    ###########################

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f'Name is {self.name}\nSalary is {self.salary}'
    def __add__(self, other):
        return self.salary + other.salary
    def __sub__(self, other):
        return self.salary - other.salary
    def __mul__(self, other):
        return self.salary * other.salary
    def __truediv__(self, other):
        return self.salary / other.salary
    def __floordiv__(self, other):
        return self.salary // other.salary

emp1 = Employee('Avi', 80000)
print(emp1)

emp2 = Employee('Ash', 55000)
print(emp2)

print(f'The sum of {emp1.name}\'s salary and {emp2.name}\'s salary is {emp1 + emp2}')
print(f'The difference of {emp1.name}\'s salary and {emp2.name}\'s salary is {emp1 - emp2}')
print(f'The product of {emp1.name}\'s salary and {emp2.name}\'s salary is {emp1 * emp2}')
print(f'The division of {emp1.name}\'s salary and {emp2.name}\'s salary is {emp1 / emp2}')
print(f'The floor division of {emp1.name}\'s salary and {emp2.name}\'s salary is {emp1 // emp2}')

print('\n'+'-'*40+'\n')

############################    LIST OPERATIONS OVERLOADING    ###########################

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['c', 'JAVA', 'Python', 'Flask']
    def __str__(self):
        return f'Name: {self.name}\nSalary: {self.salary}'
    def __len__(self):
        return len(self.tech)
    def __iter__(self):
        return iter(self.tech)            # return self.tech.__iter__
    def append(self, val):
        self.tech.append(val)
    def __getitem__(self, ind):
        return self.tech[ind]
    def __setitem__(self, key, value):
        self.tech[key] = value

emp1 = Employee('Nethai', 100000)
print(emp1)

print('Techs of', emp1.name, 'is', len(emp1))
print('List of techs of', emp1.name, '->', [t for t in emp1])

emp1.append('Streamlit')
print('List of techs of', emp1.name, '->', [t for t in emp1])

print('3rd tech is', emp1[2])

emp1[2] = 'Django'
print('Changing 3rd tech', [t for t in emp1])

print('\n'+'-'*40+'\n')

############################    PRIVATE VARIABLES    ###########################

class emp:
    def __init__(self, name):
        self.__name = name
    def __str__(self):
        return f'Name is {self.__name}'
emp1 = emp('Badrinath')
print(emp1)

print(emp1.__dict__)   # loop hole
print(emp1._emp__name)     # standard way to access private variable

print('\n'+'-'*40+'\n')

import sys
class product:
    def __init__(self, price):
        self.set_price(price)
    def get_price(self):
        return self.__price
    def set_price(self, val):
        if val < 0:
            raise ValueError("Price cannot be zero...")
        else:
            self.__price = val

try:
    pepsi = product(60)
    print(pepsi.get_price())
    #pepsi = product(-10)
    #print(pepsi.get_price())
    pepsi.set_price(80)
    print(pepsi.get_price())
except:
    print('Exception occurred...')
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])

print('\n'+'-'*40+'\n')

############################    CREATING PROPERTIES    ###########################

##### way 1
class product:
    def __init__(self, price):
        self.set_price(price)
    def get_price(self):
        return self.__price
    def set_price(self, val):
        if val < 0:
            raise ValueError("Price cannot be zero...")
        else:
            self.__price = val
    def del_price(self):
        print('Deleter called...')
        self.__price = 0

    price = property(get_price, set_price, del_price)

pepsi = product(40)
print(pepsi.price)
pepsi.price = 80
print(pepsi.price)
del pepsi.price
print(pepsi.price)

print('\n'+'-'*15+'\n')

##### way 2
class product:
    def __init__(self, price):
        self.__price=price

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, val):
        if val < 0:
            raise ValueError("Price cannot be zero...")
        else:
            self.__price = val
    @price.deleter
    def price(self):
        print('Deleter called...')
        self.__price = 0

pepsi = product(60)
print(pepsi.price)
pepsi.price = 70
print(pepsi.price)
del pepsi.price
print(pepsi.price)

print('\n'+'-'*40+'\n')

############################    INHERITANCE    ###########################

#####      MULTI LEVEL INHERIRANCE
class animal:
    def eat(self):
        print('Animals eat...')

class bird(animal): # if ANIMAL & BIRD have __init__ --> ANIMAL's __init__ got overrided !! super() is used to rectify
    def fly(self):
        print('Birds fly...')

class chicken(bird):
    def msg(self):
        print('Chicken are breeded for consumption')
    def fly(self):        #  overriding function
        print('Chicken seldom fly')

chic = chicken()
chic.eat()
chic.fly()
chic.msg()

print('\n'+'-'*40+'\n')

############################    ABSTRACTION    ###########################

from abc import ABC, abstractmethod
class Employee(ABC):

    @abstractmethod
    def do_job(self):
        pass
class Manager(Employee):
    def do_job(self):
        print('Manager\'s job...')
class Developer(Employee):
    def do_job(self):
        print('Developer\'s job')

def bankjob(emp):
    print('Bank job started...')
    emp.do_job()
    print('Bankjob ended...')

Mike = Manager()
David = Developer()

bankjob(Mike)
bankjob(David)

print('\n'+'-'*40+'\n')

############################    DUCK TYPING    ###########################

class Manager:
    def do_job(self):
        print('Manager\'s job...')
class Developer:
    def do_job(self):
        print('Developer\'s job...')

def bankjobs(emps):
    print('Bank job started...')
    for emp in emps:
        emp.do_job()
    print('Bank job completed...')

Mike = Manager()
David = Developer()
bankjobs([Mike, David])

print('\n'+'-'*40+'\n')

############################    MODULES    ###########################

import mypackage.Mymodule as m
from mypackage.Mymodule import Product

m.greet('Rahul')
print(m.sports)
print(m.runs)

p1 = Product('pringles', 120)
p1.get_details()

print('\n'+'-'*40+'\n')

############################    FILE HANDLING    ###########################
'''                       ---------====== OPENING A FILE ======----------
fl = open('data.txt', 'r')
#st = fl.read()
#st = fl.readline()
#st = fl.readlines()
print(st)
fl.close()
'''

'''                      -----====== WRITING / CREATING A FILE ======-----
file_write = open('Myfile.txt', 'w')
ch = 'y'
st = ''
while ch == 'y':
    st +=  input('Enter a line: ') + '\n'
    ch = input('Do you wanna continue: ')
file_write.write(st)
'''




# overload the operator + and > for a custom class
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
       self.name = name
       self.salary = salary

    def __gt__(self, other):
       return self.salary > other.salary

    def __add__(self, other):
       return self.salary + other.salary

emp1 = Employee('Avi', 80000)
emp2 = Employee('Ash', 55000)

print(f'The sum of {emp1.name}\'s salary and {emp2.name}\'s salary is {emp1 + emp2}')
if emp1 >= emp2:
   print(f"{emp1.name}'s salary {emp1.salary} is less than or equal to {emp2.name}'s salary {emp2.salary} ")
else:
   print(f"{emp1.name}'s salary {emp1.salary} is greater than or equal to {emp2.name}'s salary {emp2.salary} ")




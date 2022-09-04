# class with two methods get_String and print_String

class String():
    def __init__(self):
        self.inp = ""
    def get_String(self):
        self.inp = input('Enter a string: ')
    def print_String(self):
        return f'Given String: {self.inp.upper()}'

str = String()
str.get_String()
print(str.print_String())
#                             ........:::::: FUNCTIONS ::::::........

##   function definition should be on the top
##   function calling should be done after deifining
##   non-default arguments should be present in the front, later the default arguments
#          Ex :  def function_name (arg1, arg2, arg3= some_value, arg_4=0):

##  *args -> pass args like a list    =>    (value1, value2)
##  **kwargs -> pass args like a dictionary    =>   {arg1 = 'value1', arg2 = 'value2}


######################## Excercise 1 - FACTORIAL USING RECURSION
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
x=5
print('Factorial of', x, 'is', factorial(x))
print('\n\n')
############################################################


######################## Excercise 2 - FIBONACCI USING RECURSION
def fibonacci_recursion(my_val):
   if my_val <= 1:
      return my_val
   else:
      return(fibonacci_recursion(my_val-1) + fibonacci_recursion(my_val-2))
num_terms = 12
print("The number of terms is ")
print(num_terms)
if num_terms <= 0:
   print("Enter a positive integer...")
else:
   print("The Fibonacci sequence is of", num_terms, 'is', end=' ')
   for i in range(num_terms):
      print(fibonacci_recursion(i), end=' ')
print('\n\n')
############################################################


#  * multiple values can be returned only in PYTHON

#                                        dictionary as args
def extractDetails(**details):    #**details ---> kwarg
    print('Details of', details['name']+':')
    for i in details:
        print('\t', i, "=>", details[i])
extractDetails(name='Badri', age=21, qlf='Under Graduated')
print('\n\n')


#                                            DOCSTRINGS
def fun1(x, y):
    '''
        Function fun
        ------------
        res = funt(x, y)
        if x and y are integers then fun1 returns the sum of x and y
        if x and y are strings the fuek returns the concatenation of x and y
    '''
    return x + y
print(fun1(35, 55))
print(fun1.__doc__)
help(fun1)
print('\n\n')

########################   EXERCISE 3 - CELSIUS TO FAHRENHEIT USING FEATURE PROGRAMMING
cel = [23, 28, 30, 32, 36, 40, 42, 48, 50]
fah =list(map(lambda x : (x*9/5)+32, cel))     # fah = [(x*9/5)+32 for x in cel]
print('Celsius:', cel, '\nFahrenheit:', fah)
print('\n\n')
############################################################


########################   EXERCISE 4 - SORTING MONTHS USING MAP & LAMBDA
months = ['dec', 'apr', 'aug', 'may', 'feb', 'sep', 'mar', 'may', 'jul', 'jun', 'nov','jan', 'oct']
from calendar import month_name
cal_months = list(month_name)
sor_months = sorted(months, key = list(map(lambda x : x.lower()[0:3], cal_months)).index)
print("months we created:", months)
print("Sorted list of months:", sor_months)
print('\n\n')
############################################################


#                                  LIST & DICTIONARY COMPREHENSION
basic = [{x: (lambda par : 'Mr.' + par)('Sachin {}'.format(x))} for x in range(1, 6)]
print('Basics:', basic)

players = {
   'sachin': [300, 345, 225, 205, 285],
   'sourav': [200, 305, 330, 405, 150],
   'rahul': [145, 230, 298, 360, 215],
   'sehwag': [120, 150, 405, 380, 450],
   'yuvraj': [185, 205, 230, 120, 160],
   'laxman': [105, 185, 250, 385, 180]
}

plr_scr = [scr for scr in players.values()]
tot_scr = [x for r in plr_scr for x in r]
print(tot_scr)

ind_plr = {k : [scre for scre in players[k] if scre >=200] for k in players}
print(ind_plr)

glvr = 100
def fun(a):
    global a
    a = 500
    print(a)
print('before', glvr)
fun(glvr)
print('after', glvr)
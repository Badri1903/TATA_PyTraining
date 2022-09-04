#                             .......::::::: SCOPE OF VARIABLE :::::::.......

def outerfun(gname):
    info = f'Mr. {gname}'
    def innerfun():     # known as CLOSURE as it is enclosed by an function
        nonlocal info        # local variables can be accessed only as a non local variable inside an inner function
        print('hello')
        info = info + 'Tendulkar'
        print(f'Greeting {info} ')
    return innerfun

outerfun('Sachin')()
infun = outerfun('Sachin')()
print('\n\n')




#                      Applications of closure
def outerfun(greet):
    def innerfun(gname):
        print(greet, gname)
    return innerfun

enggrt = outerfun('Welcome')
tamgrt = outerfun('Vanakkam')
hingrt = outerfun('Namaskar')

enggrt('Messi')
tamgrt('Nataraj')
hingrt('Jadeja')
print('\n\n')



def outerfun(greet):
    def innerfun(sep):
        def innermostfun(gname):
            print(greet, sep, gname)
        return innermostfun
    return innerfun

enggrt = outerfun('Welcome')
tamgrt = outerfun('Vanakkam')

engsarw = enggrt('---->')
engdarw = enggrt('====>')
tamsarw = tamgrt('---->')
tamharw = tamgrt('-=##=->')

engsarw('Kane')
engdarw('Faf')
tamsarw('Raina')
tamharw('Dhoni')
print('\n\n')



def outerfun(greet):    ### with EMOJIS
    def innerfun(sep):
        def innermostfun(gname):
            import emojis
            emojized = emojis.encode(greet + ":" + sep + ":" + gname)
            print(emojized)
        return innermostfun
    return innerfun
outerfun('Vanakkam')('lion')('Siva')
print('\n\n')



def fun1():
    return('Fun1 has no args....')

def fun2(x):
    return('Fun2 has one args....{x}')

def fun3(x, y):
    return('Fun3 has two args....{x}, {y}')

def fun4(x, y, z):
    return('Fun4 has three args....{x}, {y}, {z]')

def log_details(fnc):
    loginfo = 'Logging into the systems...'
    def innerfun(*args):
        print(loginfo)
        print(fnc(*args))
        print('-'*40)
    return innerfun

infun = log_details(fun1)
infun()
print('*'*40)

infun = log_details(fun2)
infun(100)
print('*'*40)

infun = log_details(fun3)
infun(10, 20)
print('*'*40)

infun = log_details(fun4)
infun(10, 20, 30)
print('*'*40)
print('\n\n')


#######################################################################
def dif(a, b):
    return a-b

def diff(fnc):
    def indif(x, y):
        if y>x:
            x, y = y, x
        print(fnc(x, y))
    return indif

cal = diff(dif)
cal(10,50)

#############  OR         ## DECORATOR
def diff(fnc):
    def indif(x, y):
        if y>x:
            x, y = y, x
        print(fnc(x, y))
    return indif

@diff
def dif(a, b):
    return a-b

dif(10,50)
###################################################################


'''
def callme():
    print('Apples from ooty...')

def fun(fnc):
    print('Hello')
    fnc()
    print("hai")
    print('-'*10)

    def definite():
        print('Oranges frm kanpur')
    return definite

def funcallback(fnc):
    print('Mera barath')
    fnc()
    print('I love India')

funcallback(fun(callme()))
'''


def time_scale(fnc):
    def innerfun(val):
        from datetime import datetime
        st = datetime.now()
        fnc(val)
        et = datetime.now()
        print(f'The total time taken by {fnc.__name__} is {st-et}')
    return innerfun

@time_scale
def fun(max):
    l = []
    for i in range(1, max):
        for j in range(1, 1+i):
            l.append(j**2)

fun(5000)
print('\n\n\n')

###############################################################################################################

#                             .......::::::: OOPS :::::::.......

#self ---> object
#cls ---> class

class Player:           # pascal casing

    def __init__(self):
        print("Player initiated...")

    def get_runs(self):          # self refers to its object
        print("Runs scored.....")

    #def __del__(self):
     #   print("Destructor = Player deleted", self)

sachin = Player()       # object created
sachin.get_runs()
sourav = Player()
print(type(sachin))
sachin.__init__()
print('\n\n')


class player_details:
    def __init__(self):
        self.name = 'Kholi'
        self.age = 32
    def get_details(self):
        print('Name:', self.name, '\nAge:', self.age)

player1 = player_details()
player1.get_details()

player2 = player_details()
player2.name = 'Jadu'
player2.age = 29
player2.get_details()
print('\n\n')


class players:
    team = 'India'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_details(self):
        print('Name:', self.name, '\nAge:', self.age)

    @classmethod
    def chg_attr(cls, tm_name):
        cls.team = tm_name

    @classmethod
    def create_plr(cls, fname, lname, age):
        print('Factory...')
        return cls(f'{fname} {lname}', age)     #calls constructor

p1 = players('Dhoni', 30)
p1.get_details()
p2 = players('Raina', 29)
p2.get_details()
print('p1:', p1.__dict__)

p2.team = 'csk'
print('P1 team:', p1.team)
print('p2 team:', p2.team)

players.chg_attr('sahara India')
print(players.team)

p3 = players.create_plr('Mike', 'Tyson', 46)
p3.get_details()





# factorial of non negative integer

def fact(x):
    if x == 1:
        return x
    else:
        return (x * fact(x-1))

while True:
    n = int(input('Enter an positive integer: '))
    if n<0:
        print('It is a negative integer!')
    else:
        break
print('The factorial of', n, 'is', fact(n))
# sum of positive integers in a series

def series(x):
    if x-2 <= 0:
        return x
    else:
        return x+series(x-2)

while True:
    n = int(input('Enter a non-negative integer: '))
    if n>=0:
        print('The sequential sum of', n, 'is', series(n))
        break
    else:
        print('It\'s a negative integer!\nKindly enter a POSITIVE integer')
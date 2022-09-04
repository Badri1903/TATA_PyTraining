# sum of non negative integer

def sum_number(x):
    if x/10 == 0:
        return x
    else:
        digit = x%10
        return digit + sum_number(x//10)

while True:
    n = int(input('Enter a non-negative integer: '))
    if n>=0:
        print('The sum of', n, 'is', sum_number(n))
        break
    else:
        print('It\'s a negative integer!\nKindly enter a POSITIVE integer')


# calculate a to the power of b

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)

a = int(input('Enter the base: '))
b = int(input(('Enter the exponent: ')))
print(f'{a} to the power of {b} is {power(a, b)}')
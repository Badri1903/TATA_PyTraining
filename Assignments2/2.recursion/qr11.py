# recursive GCD

def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(b, a - b)


x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
print(f'Gcd of {x} and {y} is {gcd(x, y)}')

# geometric sum

def geometric_sum(x, y, z):
    if z == 1:
        return x
    else:
        return x*((y**z-1)/(y-1)) + geometric_sum(x, y, z-1)

a = int(input('Enter a positive number: '))
r = float(input('Enter common ratio: '))
n = int(input('Enter the number of successive terms: '))

print("The geometric sum of {} with common ratio of {} between {} successive terms is {:.2f}".format(a, r, n, geometric_sum(a, r, n)))
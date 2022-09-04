# harmonic sum

def harmonic_sum(x):
    if x < 2:
        return 1
    else:
        return 1/x + harmonic_sum(x-1)

n = int(input('Enter a positive number: '))
print("The harmonis sum of {} is {:.2f}".format(n, harmonic_sum(n)))
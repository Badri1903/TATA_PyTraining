#Assignment 1
n = 1
for i in range(1, 5):
    for j in range(1, i+1):
        print(n, end="")
        n=n+1
    print("")
print("\n\n")

#Assignment 2
for i in range(1,6):
    for j in range(1, i+1):
        print(1, end = "")
    print("")
print("\n\n")


#Assignment 3
n=1
for i in range(1, 6):
    for j in range(1, i+1):
        print(n, end="")
    n+=1
    print("")
print("\n\n")

#Assignment 4
n = 10
n1, n2, series = 0, 1, 0
for i in range(n):
    print(series, end=" ")
    n1 = n2
    n2 = series
    series = n1 + n2
print("\n\n")


#Assignment 5
print("Magic Numbers:", end=" ")
for n in range(100, 100000):
    factorial = 0
    for i in str(n):
        fact = 1
        for j in range(1, int(i)+1):
            fact *= j
        factorial = factorial + fact
    if n == factorial:
        print(n, end=" ")
print("\n\n")


#Assignment 6
size = 5
n = 1
for i in range(1, size + 1):
    for j in range(size, i - 1, -1):
        print(" ", end="")
    for k in range(0, i):
        print(n, end=" ")
        n += 1
    n = 1
    print()
for i in range(1, size):
    for j in range(0, i+1):
        print(" ", end="")
    for k in range(size - i):
        print(n, end=" ")
        n += 1
    n = 1
    print()
print("\n\n")


#Assignment 7
n = 6
element = 1
for i in range(0, n):
    print(element)
    for j in str(a):
        print(j, end=" ")
    print("")
print('\n\n')


#Assignment 8
possible_num_mangoes=[]
for n in range(100):
    temp = n
    times = 0
    for i in range(0, 3):
        if (temp)%3 == 1:
            part = ((temp-1)/3)+1
            temp = temp - part
            times += 1
    if times == 3:
        possible_num_mangoes.append(n)
print('Possible number of mangoes:', possible_num_mangoes)
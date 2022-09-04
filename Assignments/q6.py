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
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
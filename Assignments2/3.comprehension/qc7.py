a = [[j for j in range(1, 1001) if j%i == 0] for i in range(2, 10)]
num = 2
for i in a:
    print(num, '->', i)
    num+=1
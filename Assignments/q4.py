n = 10
n1, n2, series = 0, 1, 0
for i in range(n):
    print(series, end=" ")
    n1 = n2
    n2 = series
    series = n1 + n2
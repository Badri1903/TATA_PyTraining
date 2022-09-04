# matrix transpose

rows = int(input('Enter the number of rows: '))
columns = int(input(('Enter the number of columns: ')))

mat = []
for i in range(rows):
    a = []
    for j in range(columns):
        a.append(0)
    mat.append(a)

for i in range(rows):
    for j in range(columns):
        mat[i][j] = int(input(f'Enter the [{i}] [{j}] element: '))

print('Matrix:', mat)

transpose = [[mat[j][i] for j in range(rows)] for i in range(columns)]
print('Transpose:', transpose)
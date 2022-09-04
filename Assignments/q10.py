n=3
arr=[]
print(f"\n{n}*{n} Identity matrix")
for i in range(n):
    el = []
    for j in range(n):
        if i==j: el.append(1)
        else: el.append(0)
    arr.append(el)
for a in  arr:
    print(a)
possible_num_mangoes=[]
for n in range(1000):
    temp = n
    times = 0
    for i in range(0, 3):
        if (temp)%3 == 1:
            part = ((temp-1)/3)+1
            temp = temp - part
            times += 1
    if times == 3:
        if temp%3 == 0 and temp/3 > 0:
            possible_num_mangoes.append(n)
print('Possible number of mangoes:', possible_num_mangoes)
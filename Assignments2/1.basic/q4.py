# genrating dictionaries

n = int(input('Enter number of items: '))
square_dic = {}
for i in range(1, n+1):
    square_dic.update({i: i*i})
print('Square table dictionary:', square_dic)
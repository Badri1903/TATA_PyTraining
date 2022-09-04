# remove all occurence of a specific item

list_dup = [1,1,1,3,4,6,8,7,5,3,1,1,3,1,1,8,1,9,1,0,1,1,1,6,4,2,3,5,3]

x = int(input('Enter an element to be removed: '))
for i in range(list_dup.count(x)):
    list_dup.remove(x)
print('Given list:', list_dup)
print(x, 'removed list:', list_dup)
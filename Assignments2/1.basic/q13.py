# count of each element

list_sample = [1,1,1,3,4,6,8,7,5,3,1,1,3,1,1,8,1,9,1,0,1,1,1,6,4,2,3,5,3]
set_list_sample = set(list_sample)
print('Given list:', list_sample, '\n')

def decoration(element, recurrence):
    print("{0:^7}{1:^13}".format(element, recurrence))

decoration('Element', 'Recurrence')
for i in set_list_sample:
    decoration(i, list_sample.count(i))
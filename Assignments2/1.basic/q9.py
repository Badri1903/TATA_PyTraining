# sum all the items in a list

list_sample = [1,1,1,3,4,6,8,7,5,3,1,1,3,1,1,8,1,9,1,0,1,1,1,6,4,2,3,5,3]

sum_fun = sum(list_sample)   # method 1
print('Using sum function:', sum_fun)

list_sum = []   # method 2
sum = 0
for i in list_sample:
    sum = sum+i
print('Using loop:', sum)
# reversing list

sample_list = ['badri', 'abi', 'anu', 'nethu', 'avi', 'ash', 'gayu']
print('Given list:', sample_list)

rev_list = sample_list[::-1]    # method 1
print('Reversing list using slicing operator:', rev_list)

new_list = []    # method 2
for element in sample_list:
    new_list.insert(0, element)
print('Reversing list using another list:', new_list)

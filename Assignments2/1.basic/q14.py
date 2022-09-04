# finding common elements

sample_list1 = ['gayu', 'badri', 'abi', 'anu', 'nethu', 'avi', 'viji']
print('List 1:', sample_list1)
sample_list2 = ['tomboy', 'praveen','viji', 'hari', 'avi', 'ash', 'gayu']
print('List 2:', sample_list2, '\n')

common_ele = []
for i in sample_list1:
    if i not in common_ele:
        if i in sample_list2:
            common_ele.append(i)
print('Common elememnts:', common_ele)



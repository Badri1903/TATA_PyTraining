# removing duplicates

sample_dic = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60, 3:30, 7:70, 4:40, 8: 80}
print("Given dictionar:", sample_dic)

result_dict = {}
for k, v in sample_dic.items():
    if v not in result_dict.values():
        result_dict.update({k: v})
print('After removing duplicates:', result_dict)

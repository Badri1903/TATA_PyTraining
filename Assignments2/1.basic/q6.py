# getting key of minimun value

sample_dic = {2:20, 3:30, 4:40, 5:50, 6:60, 1: 10, 3:30, 7:70, 4:40, 8: 80}
print("Given dictionar:", sample_dic)

for k, v in sample_dic.items():
    if v == sorted(sample_dic.values())[0]:
        print('Key of minimum value from the given dictionary:', k)

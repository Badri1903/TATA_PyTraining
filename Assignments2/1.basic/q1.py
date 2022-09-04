# concatenating dictionaries

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
print('Dictionary 1:', dic1, '\nDictionary 2:', dic2, '\nDictionary 3:', dic3, '\n')

dic_tot1 = dic1 | dic2 | dic3
print('Concatenating dictionaries using \'|\' operator:', dic_tot1)    # method 1

dic_tot2 = {**dic1, **dic2, **dic3}
print('Concatenating dictionaries using \'**\' operator:', dic_tot2)    # method 2

list_dic = [dic1, dic2, dic3]
tot_dic = {}
for dict in list_dic:    # method 3
    for k, v in dict.items():
        tot_dic.update({k:v})
print('Concatenating dictionaries using for loop:', tot_dic)

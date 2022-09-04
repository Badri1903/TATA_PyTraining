s="badri"
print(s.index('r'))
print(s.find('r'))
#print(s.index('R'))
print(s.find('R'))


print("\n\n")
lst1 = [1,2,3,4]
print("..copy()")
print("Lst1 before:", lst1)
lst2 = lst1.copy()   #deep copy
print("lst2 before:", lst2)

lst2.extend([5,6,7])
print("lst1 after:", lst1)
print("lst2 after:", lst2)



print("..sorts()")
sor1 = [1,2,4,3,6,5,8,7]
sor2 = sorted(sor1)
print("sorted:", sor2)
print("original after sorted:", sor1)
sor1.sort()
sor3 = sor1
print("sort:", sor3)
print("original after sort:", sor1)

print("\n")
random_list = [1,234,1023,452,453,10935]
normal_sort = sorted(random_list)
print("Normal sort:", normal_sort)
ascii_sort = sorted(random_list, key=ascii)
print("sort based on ascii:",ascii_sort)
letter_list = ['asd', 'nv', 'kjbkj', 'sdr']
length_sort = sorted(letter_list, key = len)
print("sort based on length:", length_sort)
print('\n')

# ASSIGNMENT
months = ['dec', 'apr', 'aug', 'may', 'feb', 'sep', 'mar', 'may', 'jul', 'jun', 'jan', 'oct']
from calendar import month_name
print("month names:", month_name)
cal_months = list(month_name)
print("month names:", cal_months)
def fun(mon):
    for i in cal_months:
        if mon.capitalize() in i:
            return cal_months.index(i)
sor_months = sorted(months, key=fun)
print("months we created:", months)
print("Sorted list of months:", sor_months)



# dictionary
print('\n\n')
profile = {'name': 'badri', 'age': 21, 'place': 'sirkali'}
profile['dep'] = 'tbu'
profile['competency'] = 'anv'
print(profile)
for k in  profile:
    print(k, '=>', profile[k])
del profile['competency']
print(profile)
#print(profile['gender'])   ---> throws error
print(profile.get('name'))
print(profile.get('gender', '\"!Gender hasn\'t been entered\"\n'))

profile.setdefault('competency', 'anv')
profile.setdefault('dep', 'mcv')      # dep key already present so it won't change
print(profile, '\n')

new_profile = dict.fromkeys(profile, 'enter-value')
print(new_profile,'\n')

empl ={'33108': {'name': 'badri', 'age': 21, 'place': 'sirkali'}, '33110':  {'name': 'nethaj', 'age': 21, 'place': 'tirupur'}}
for id, info in empl.items():
    print(id)
    for k, v in info.items():
        print('\t', k + ":", v)
    print('')

fst = frozenset([1, 2, 3, 4])
print(fst)
print(type(fst))

sample_set = {1,2,3,4,5}
sample_set.discard(6)
print(sample_set)

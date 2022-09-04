#PALINDROME
st = 'madam'
if st == st[::-1]: print("Palindrome", "\n")
else: print("Not palindrome", "\n")


#FINDING DESIRED LETTERS
st = "Hello lTuesday"
pos = st.find("l", st.find("l")+1)
print("Position of 2nd 'l':", pos, "\n")


#C SYNTAX
sentence = "Name: %s, Age: %d, weight: %.2f"
values = ("Badri", 21, 65.7899)
print(sentence %values)
print(sentence %("Avi", 22, 73.6), "\n")


#UNIX STYLE
from string import Template
temp = Template("I'm $name. I'm $age years old")
print(temp.substitute(name="Badri", age=21),"\n")


#FORMAT METHOD
print("Hai {}!, I'm {}" .format("Abi", "Badri"))
print("Hai {1}!, I'm {0}" .format("Badri", "Dany"))
print("Hai {new}!, I'm {me}" .format(new="Abi", me="Badri"))

print("\nThe number {num:10}, {num:f}, {num:b}".format(num = 345))
print("{:.5}".format("Badrinath"))

from math import pi
print("{pi:10.3}".format(pi=pi))     #blank spaces other than the value in 10 spaces
print("{pi:010.4}".format(pi=pi))    #0's other than the value in 10 spaces

print("{0:.<70}{1:.>5}\n".format("Python basics", 30))

#HEADINGS
print("{0:{1}^{2}}".format("Hello world", "=", 40))
print("{txt:=^40}".format(txt="Hello world"))
print("Hello world".center(40, "="))
print("Hello world".center(40, "="))



letters = ['a', 'b', 'c', 'd', 'e']
for letter in enumerate(letters):
    print(letter, " ", end = "")
print()

for letter in enumerate(letters):
    print(letter[0], letter[1])
print('\n')

for index, letter in enumerate(letters):
    print(index, letter)

myl = [[1,2,3], [4,5,6], [7,8,9]]
for idx, lst in enumerate(myl):
    print("List",idx)
    for idx, num in enumerate(lst):
        print("\t", idx, "\t", num)




# ASSIGNMENT
def decoration(item, price):
    print("{0:<40}{1:>20}".format(item, price))
print("="*60)
decoration("item", "price")
print("="*60)
decoration("Apple", 150)
decoration("Chocolate", 200)
print("="*60)




n=3
arr=[]
print(f"\n{n}*{n} Identity matrix")
for i in range(n):
    el = []
    for j in range(n):
        if i==j: el.append(1)
        else: el.append(0)
    arr.append(el)
for a in  arr:
    print(a)


lst = [1,2,1,3,1,4,1,1,1,1,1,5,1,6,1,7,8]
while lst.count(1):
    lst.remove(1)
print(lst)


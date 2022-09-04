print(__name__)
a, b, c = 1, True, "Badri"    #multi variable assignment
print(a,b,c)
print(a,b,c, sep='')


#Default adding
print(2+3.5)    #float


#Number conversions
print("conversions".center(40, "-"))
n = 100
print(bin(a))
print(oct(a))
print(hex(a))


#Printing statement styles
a='ram'
b='kumar'
print("First name: "+a+" and Last name: "+b)
print(f"First name: {a} and Last name: {b}")


#Printing prime numbers between 150 and 50
a=[]
for i in range(150, 51, -1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        a.append(i)
print(a,"\nNumber of prime numbers between 150 and 50:",len(a))
print("\n\n")

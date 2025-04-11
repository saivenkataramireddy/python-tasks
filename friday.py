
#Removing special character's from the string
n=input("Enter a string")
a=""
for i in n:
    if i.isalpha():
        a = a+i
print(a)

#Removing brackets in algebric expression
n=input("Enter a string")
a=""
for i in n:
    if i!="("and i!=")":
        a +=i
print(a)

# program to print sum of digits in a number
n=input("number")
a=0
for i in n:
    a += int(i)
print(a)
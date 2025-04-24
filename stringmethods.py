
n=input("Enter a string")
a=""
b=""
for i in n:
    if i>='A' and i<='Z':
        a+=i
    else:
        b+=i
print(f"{a}{b}") 

#print even length words
n="This is a python language".split()
a=""
for i in n:
    b=len(i)
    if b%2==0:
        a +=i+" "
print(a)

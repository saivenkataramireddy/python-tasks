#Program to print maximum odd digit in the given number
num=input("Enter a number")
a=0
for i in num:
    i=int(i)
    if i%2!=0 and i>a:
        a =i
if a>0:
    print(f"{a}is the max odd number")
else:
    print("There is no odd numbers")

# Program to print count of special characters in the given string

n=input("Enter a string")
count=0
for i in n:
    if i>='a' and i<='z' or i>='A' and i<='Z'and i==" " or i>='0' and i<='9':
        continue
    else:
        count +=1
print(count)
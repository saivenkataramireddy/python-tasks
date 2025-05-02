#Check if the number is a Harshad(or Niven) number or not.
n=input("Enter")
a=0
for i in n:
    a += int(i)
if int(n)%a==0:
    print("harshad")
else:
    print("Not harshad")

#2)Check if the number is an abundant number or not.
n=int(input("Enter"))
a=0
for i in range(1,n):
    if n%i ==0:
        a += i
if a>n:
    print("Abundant number")
else:
    print("Not an abundant number")

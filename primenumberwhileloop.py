n=int(input("Enter a number"))
i=2
while i<=(n//2)+1:
    if i ==0:
        pass
    if n%i==0:
        print("Not Prime")
        break
    i+=1
else:
    print("Prime")
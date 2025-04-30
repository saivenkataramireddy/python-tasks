n=input("Enter a number")
a=0
prime=0
for i in n:
    b=int(i)
    if b>1:
        for j in range(2,(b // 2)+1):
            if b%j==0:
                a = j
                break
        else:
            prime = j
            print(j,"is prime")
        
    else:
        print(a,"not")
print("There are no primes")
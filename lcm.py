n1,n2=list(map(int,input().split()))
max1=max(n1,n2)
while True:
    if max1%n1==0 and max1%n2==0:
        print("LCM",max1)
        break
    max1+=1
min1=min(n1,n2)
while True:
    if n1%min1==0 and n2%min1==0:
        print("Gratest Common Divisor",min1)
        break
    min1 -=1
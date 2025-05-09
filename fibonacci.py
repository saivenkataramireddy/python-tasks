n=int(input("Enter"))
a,b=0,1
while b<n:
    a,b=b,a+b
if n==b or n==0:
    print(n,"Fibonacci number")
else:
    print("No it is not a fib number")


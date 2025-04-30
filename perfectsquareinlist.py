#1) WAP to print perfect square numbers in the list ? 
n=list(map(int,input("Enter a list").split()))
for i in n:
    if (i**0.5)==int(i**0.5):
        print(i)
#2) WAP to print all the decimals numbers in the given input ?
n=input("Enter").split()
for i in n:
    if "." in i:
        print(i)
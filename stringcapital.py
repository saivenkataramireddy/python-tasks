n=input("Enter")
a="" 
for i in n:
    if i==" ":
        if len(a)==1:
            print(a.upper(),end=" ")
        else:
            print(a[0].upper()+a[1:len(a)-1]+a[-1].upper(),end=" ")        
        a=""
    else:
        a = a+i  
print(a[0].upper()+a[1:len(a)-1]+a[-1].upper(),end=" ")
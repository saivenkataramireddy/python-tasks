n=list(map(int, input("Enter a list of prime numbers").split()))
maximum=0
minimum=0
for i in n:
    if i>1:
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            if minimum==0 or  i<minimum:
                minimum=i
            else:
                if maximum==0 or i> maximum:
                    maximum=i
print(maximum+minimum)
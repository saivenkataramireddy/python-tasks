# num=list(map(int,input().split()))
# target=int(input())
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         if num[i]+num[j]==target:
#             print(i,j)
s=input()
rom={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
for i in s:
    for j in i:
        c=0
        for k,v in rom.items():
            if j==k:
                c+=v
print(c)
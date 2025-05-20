# n=list(map(int,input().split()))
# nums=[]
# zero=[]
# for i in n:
#     if i==0:
#         zero.append(i)
#     else:
#         nums.append(i)
# print(*nums,*zero)

n=[int(i) for i in input().split()]
res=n[0]
def lcm(n1,n2):
    max1=max(n1,n2)
    if max1%n1==0 and max1%n2==0:
        return max1
    max1 +=1
for i in n[1:]:
    res=lcm(res,i)
print("Least Common multiple",res)
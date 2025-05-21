# arr={12, 10, 9, 45, 2, 10, 10, 45}
# print(set(arr))

arr=input().split()
unic=[]
for i in arr:
    if i not in unic:
        unic.append(i)
print(unic)

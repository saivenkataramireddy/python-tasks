n=input("Enter").split()
mid=n[1:-1]
mid.reverse()
res=[n[0]] + mid + [n[len(n)-1]]
print(" ".join(res))
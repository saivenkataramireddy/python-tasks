#palindrome using string slicing
'''
s=input("Enter a string")
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
'''
s=input("Enter a string")
v="AEIOUaeiou"
vowels=0
cons=0
spaces=0
for i in s:
    if i==" ":
        spaces +=1
    elif i in v:
        vowels +=1
    else:
        cons +=1
print("Vowels",vowels)
print("Consonents",cons)
print("spaces",spaces)
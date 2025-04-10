#printing vowels and consonents in a word
'''n=input("Enter a string")
a="aeiouAEIOU"
vowels=""
cons= ""
for i in n:
    if i in a:
        vowels +=i
    else:
        cons +=i
print("Vowels",vowels)
print("Consonents",cons)'''
#printing count of vowels and consonents
n=input("Enter a string")
a="aeiouAEIOU"
vowels=0
cons=0
for i in n:
    if i in a:
        vowels +=1
    else:
        cons +=1
print("vowels",vowels)
print("Consonents",cons)

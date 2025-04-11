
#WAP to remove spaces from the given string
n=input("Enter a string")
a="" 
for i in n:
    if i!=" ":
        a += i
print(a)

#WAP to check whether vowels are more or consonants are more

n=input("Enter string")
a="AEIOUaeiou"
vowels=" "
cons=" "
for i in n:
    if i in a:
        vowels += i
    else:
        cons += i
if len(vowels)==len(cons):
   print("Both are same")
elif len(vowels)>len(cons):
    print("Vowels are more")
else:
    print("consonents are more")

print("vowels",vowels)
print("Consonent",cons)
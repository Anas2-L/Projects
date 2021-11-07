def anagram(x1,x2):
    if len(x1)!=len(x2):
        return False
    if(sorted(x1)==sorted(x2)):
        return True

x1=input("enter first string\n")
x2=input("enter second string\n")

print(anagram(x1,x2))

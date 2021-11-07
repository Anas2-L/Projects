def contanvowels(string):
    countv=0
    countc=0
    vowels="aeiou"
    for char in string.lower():
        if char in vowels:
            countv+=1
        else:
            if(char !=" "):
                countc+=1
    print(countc," ",countv)

contanvowels("I aba abb abbbaa")

    
            



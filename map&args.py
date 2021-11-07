mystr = input("Please type a sentence: ")

print(list(map(mystr.lower().count, "aeiou")))

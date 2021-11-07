def palindrome(x):
    return(x==reverse(x))

def reverse(x):
    x1=x[::-1]
    return x1

x=input("Enter the string\n")
print(palindrome(x))

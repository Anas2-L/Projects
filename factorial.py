def fact(x):
    result=1
    for i in range(1,x+1):
        result=result*i
    return result

x=int(input("Enter the number\n"))
print(fact(x))
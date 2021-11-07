num=int(input("Enter a number"))
temp=num
while (temp>=1):
    if(temp%10==0):
        print(0)
    else:
        print(int(temp%10))
    temp=int(temp/10)

print(num)
def sumlist(list1):
    sum=0
    for i in list1:
        sum=sum+i
    return sum

list1=[]
while(True):
    try:
        x=int(input("add numbers to the list\n"))
        list1.append(x)
    except ValueError:
        break
print(list1)    

print(sumlist(list1))

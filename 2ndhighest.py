def secondhigh(list1):
    new_list=set(list1)
    new_list.remove(max(new_list))
    return max(new_list)

list1=[]
n=int(input("enter list size "))
for i in range(n):
    x=input("\nenter the element ")
    list1.append(x)

print("original list\n",list1)
print(secondhigh(list1))




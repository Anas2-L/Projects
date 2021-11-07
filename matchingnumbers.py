list1=[1,1,1,3,3,2]
listcount=list(map(list1.count,set(list1)))
print(dict(zip(set(list1),listcount)))
      

def occurences(x,string):
    count1=0
    print(string.count(x))
    for i in string:
        if(i==x):
            count1+=1
    print(count1)

string=input("enter the string\n")
x=input("enter character to be searched\n")
occurences(x,string)

    

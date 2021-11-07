def factr(x):
    if(x<=1):
        return x
    else:
        return (x*factr(x-1))

print(factr(5))

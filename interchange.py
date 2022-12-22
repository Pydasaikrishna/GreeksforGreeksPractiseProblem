def swap_list(l):
    size=len(l)
    temp=l[0]
    l[0]=l[size-1]
    l[size-1]=temp
    return l

l=[10,20,30,40,50,60]
print(swap_list(l))
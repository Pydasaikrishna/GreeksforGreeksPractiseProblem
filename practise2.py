#write a python function that takes two lists and returns True if they have at least one common member


def common_Num(l1,l2):
    result = False
    for i in l1:
        for j in l2:
            if(i==j):
                result = True
                return result
print(common_Num([1,2,3,4,],[3,4,5,6]))
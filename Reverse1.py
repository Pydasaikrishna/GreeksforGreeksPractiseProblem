def reverse_list(arr):
    left=0
    right=len(arr)-1
    while (left < right):
        temp = arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left += 1
        right -= 1

    return arr


# arr = [10,20,30,40,50,80,90,100]
arr=[]
n=int(input("Enter Entries: "))
for i in range(0,n):
    data=int(input())
    arr.append(data)
print("Previous value",arr)
print("After Reverse",reverse_list(arr))
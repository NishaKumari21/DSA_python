def linearsearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

arr=[2,3,4,5,7,8]
x=8
result=linearsearch(arr,x)
print("searching element at index",result)
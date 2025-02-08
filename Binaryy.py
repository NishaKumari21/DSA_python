def binary_s(arr,x,low,high):
    if high>=low:
       mid=(low+high)//2
       if arr[mid]==x:
          return mid
       elif arr[mid]>x:
         return binary_s(arr,x,low,mid-1)
       else:
         return binary_s(arr,x,mid+1,high)
    return -1

arr=(2,8,4,7,9,10,12)
x=9
low=0
high=len(arr)-1
result=binary_s(arr,x,low,high)
print(result)
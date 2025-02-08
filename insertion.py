def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        # key is the element to be compared
        key=arr[i]
        # move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j=i-1
        # shift elements of arr[0..j] that are greater than key, to one position ahead of their current position
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key
    return arr
arr=[6,90,4,23,89,45]
result=insertion_sort(arr)
print(result)
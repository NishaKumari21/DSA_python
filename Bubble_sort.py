def bubble_sort(arr):
    # amde a function here
    n=len(arr)
    # value of n is equal to the length of array
    for i in range(n):
        # last i elements are already sorted, no need to check them again
        for j in range(0,n-i-1):
            # after every phase the last element is getting sorted so no need to sort them again
            # if current element is greater than the next one, swap them
            if arr[j]>arr[j+1]:
                # swap the element
                arr[j],arr[j+1]=arr[j+1],arr[j]
                # after swapping, the largest element will be at the end of the unsorted subarray, so we don't need to check it again
# driver code
arr=[7,2,9,12,90,23,56]
bubble_sort(arr)
print("your bubble sorted array is :",arr)
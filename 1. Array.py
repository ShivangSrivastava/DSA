def linear_search(element, arr):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

def binary_search(element,arr):
    start = 0
    end = len(arr)-1
    
    while start<end:
        mid = (start+end)//2
        if arr[mid]==element:
            return mid
        if arr[mid]<element:
            start = mid
        else:
            end=mid
    return -1

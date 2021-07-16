"""
## Binary Search Steps:

- Compare x with the middle element.
- If x matches with the middle element, we return the mid index.
- Else if x is greater than the mid element, 
    - Then x can only lie in the right (greater) half subarray after the mid element. 
    - Then we apply the algorithm again for the right half.
- Else if x is smaller, the target x must lie in the left (lower) half. 
    - So we apply the algorithm for the left half.

"""

def binarySearch(arr, left, right, target):
    """ 
    Recursive Implementation of Binary Search 
    """
    if right >= left:
        # get midpoint
        mid = (left + right) // 2
        
        # if midpoint == target 
        if arr[mid] == x:
            return mid
        
        # if midpoint value > target --> move to left side of midpoint
        elif arr[mid] > target:
            return binarySearch(arr, left, mid-1, target)
        
        # if midpoint value < target --> move to right side of midpoint
        else:
            return binarySearch(arr, mid+1, right, target)
    else:
        return -1

arr = [2,3,4,10,40]
x = 10
idx = binarySearch(arr,0,len(arr)-1,10)
print(idx)
"""
## Sort Array
rr
Link: https://leetcode.com/problems/sort-an-array/
        
Given an array of integers nums, sort the array in ascending order.

Example
```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
```

### Explanation 

For this problem, we will implement, `Quicksort`. The performance will depend
upon the position of the pivot with worse case O(n2) and best case being O(n
log n). 

- Iterate over each element in the list and check if it's smaller than the pivot. 

- The pivot splits the list in half and is often taken as the median of
  initial, mean, and ending value of the list. 
- Next, move the pivot value to index_0.   

- Now we will have two pointers, "i" at index_1 and "j" at index_2. We will
  loop over the list and check if j is less than the  pivot, if so we will swap
  the values of i and j advance the pointers. In this case, everything less
  than the index of i is less than the pivot value and everything to the right
  of i is greater than the pivot value. If j is greater than the pivot value,
  keep incrementing the index of j to to the end of list. 

- Next swap the pivot value with value in index i.
    - smaller == left partition
    - larger == right partition
- This is a recursive function and we can now call the quick sort algorithm on
  the left hand and right hand side of the list.  

[Reference](https://www.youtube.com/watch?v=uXBnyYuwPe8)
[Reference](https://www.youtube.com/watch?v=CB_NCoxzQnk)

"""
from typing import List


class QuickSort:
    """Quicksort Implementation"""

    def __init__(self):
        self.threshold = 1

    def sort(self, arr: List[int]):
        self.helper(arr, low=0, high=len(arr) - 1)
        return arr

    def helper(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.helper(arr, low, p - 1)
            self.helper(arr, p + 1, high)

    def get_pivot(self, arr, low, high):
        """get median pivot value"""
        mid = (high + low) // 2
        s = sorted([arr[low], arr[mid], arr[high]])
        if s[1] == arr[low]:
            return low
        elif s[1] == arr[mid]:
            return mid
        return high

    def partition(self, arr, low, high):
        pivotIndex = self.get_pivot(arr, low, high)
        pivotValue = arr[pivotIndex]
        arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]
        border = low

        # iterate over array
        for i in range(low, high + 1):
            if arr[i] < pivotValue:
                border += 1
                # swap with border
                arr[i], arr[border] = arr[border], arr[i]

        # swap pivot value into the border position
        arr[low], arr[border] = arr[border], arr[low]

        return border


n = [5, 2, 3, 1]
q = QuickSort().sort(n)
print(q)

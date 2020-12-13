from typing import List

def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    red, white, blue = 0, 0, 0
    for i in nums:
        if i == 0:
            red += 1
        elif i == 1:
            white += 1
        elif i == 2:
            blue += 1

    nums[:] = [0] * red + [1] * white + [2] * blue
    return nums

def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    encode = {i: str(s[idx]) for idx, i in enumerate(indices)}
    string = "".join([encode[i] for i in range(0, len(indices))])
    return string


class QuickSort:
    """  Quicksort Implementation"""

    def __init__(self):
        self.threshold = 1

    def sort(self, arr:List[int]):
        self.helper(arr, low=0, high=len(arr)-1)
        return arr

    def helper(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.helper(arr, low, p - 1)
            self.helper(arr, p + 1, high)

    def get_pivot(self, arr, low, high):
        """ get median pivot value"""
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
        for i in range(low, high+1):
            if arr[i] < pivotValue:
                border += 1
                #swap with border
                arr[i], arr[border] = arr[border], arr[i]
        
        # swap pivot value into the border position
        arr[low], arr[border] = arr[border], arr[low]

        return border
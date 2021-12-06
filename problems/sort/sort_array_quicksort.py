"""
Sort Array

Reference: https://leetcode.com/problems/sort-an-array/
        
Given an array of integers nums, sort the array in ascending order.

Example
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Solution: Quick Sort  
Time Complexity: O(nlogn)
Reference 1: https://www.youtube.com/watch?v=uXBnyYuwPe8
Reference 2: https://www.youtube.com/watch?v=CB_NCoxzQnk

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


if __name__ == "__main__":
    n = [5, 2, 3, 1]
    q = QuickSort().sort(n)
    print(q)

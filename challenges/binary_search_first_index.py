"""
Given an array of integers nums sorted in ascending order, find the starting
index a given target 

Solution is O(log n) runtime complexity.

"""
from typing import List


def binary_search(nums: List[int], target: int) -> List[int]:
    """Implement Binary Search to find start index of given target"""
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:  # mid == target
            # first index of array - edge case
            if mid - 1 < 0:
                return mid
            # found first element
            if nums[mid - 1] != target:
                return mid
            # move right pointer
            else:
                right = mid - 1
    return mid


if __name__ == "__main__":
    # idx = [0    1    2    3     4    5
    nums = [100, 105, 110, 115, 115, 150]
    target = 110
    print(binary_search(nums, target))

"""
Find First and Last Position of Element in Sorted Array

Reference:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Solution: Binary Search
Time Complexity: O(log n)
"""


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = 0
    right = len(nums) - 1
    results = []

    while left <= right:

        # Find the mid point
        mid = (left + right) // 2

        # if target is found to left of mid
        if nums[mid] == target and nums[mid - 1] == target:
            results.append(mid - 1)
            right = mid - 1

        # if target is found to right of mid
        elif nums[mid] == target and nums[mid + 1] == target:
            results.append(mid + 1)
            left = mid + 1

        # Search right side
        elif nums[mid] < target:
            left = mid + 1

        # Search left side -- > nums[mid] > target
        else:
            right = mid - 1

    if not results:
        return [-1, -1]
    else:
        return results


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(searchRange(nums, target))

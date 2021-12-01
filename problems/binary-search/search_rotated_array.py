"""
Search in Rotated Sorted Array

Reference: https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

Solution: a brute force approach is to iterate through the array and find if
the index of the array equals the target. But we need to write a solution is is
O(log n) time complexity. 

Solution: Binary Search 
Reference: https://www.youtube.com/watch?v=U8XENwh8Oy8&t=18s
"""


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    # Set pointers
    left, right = 0, len(nums) - 1

    # Binary Search
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # check to see if search the left or right side of the array
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid = 1

        # search the right half
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1

    return left


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(search(nums, target))

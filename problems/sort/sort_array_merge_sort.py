""" 
Sort an Array

Reference: https://leetcode.com/problems/sort-an-array/

Given an array of integers nums, sort the array in ascending order.

Example:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Solution: Implement merge sort algorithm
Time Complexity: O(nlogn)
"""


def sortArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = sortArray(nums[:mid])
    right = sortArray(nums[mid:])

    print("left", left)
    print("right", right)
    return merge(left, right)


if __name__ == "__main__":
    nums = [5, 2, 3, 1]
    print(sortArray(nums))

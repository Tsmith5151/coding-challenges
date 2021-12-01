""" 
Squares of a Sorted Array

Reference: https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Solution: two pointers (left and right)
Time Complexity: O(n)
"""


def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left = 0
    right = len(nums) - 1
    results = []
    while left <= right:
        if abs(nums[right]) >= abs(nums[left]):
            results.append(nums[right] ** 2)
            right -= 1
        else:  # abs(nums[right]) < abs(nums[left])
            results.append(nums[left] ** 2)
            left += 1
    return results[::-1]


if __name__ == "__main__":
    nums = [-7, -3, 2, 3, 11]
    print(sortedSquares(nums))

"""
Find peak element

Reference: https://leetcode.com/problems/find-peak-element/	


A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Example:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak
element is 2, or index number 5 where the peak element is 6.

Solution: Binary Search
Time Complexity: O(log n)
"""


def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    left = 0
    right = len(nums) - 1
    while left < right:
        # compute midpoint
        mid = left + (right - left) // 2

        # check if midpoint is peak
        if mid - 1 >= 0 and nums[mid - 1] <= nums[mid]:
            left = mid
        else:
            right = mid - 1

    return nums[left + 1]


if __name__ == "__main__":
    # nums = [1, 2, 1, 3, 5, 6, 4]
    nums = [6, 5, 4, 3, 2, 3, 2]
    print(findPeakElement(nums))

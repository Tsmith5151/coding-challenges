"""
Contains Duplicate

Reference: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Solution: Hash Map
Time Complexity - O(n)
Memory Complexity - O(n)

Second Solution: Sorting
Time Complexity: O(nlogn)
Memory Complexity: O(1) # no extra memory is used
"""


def containsDuplicate1(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    counter = {i: 0 for i in range(len(nums))}
    for num in nums:
        counter[num] = 1 + counter.get(num, 0)
        if counter[num] > 1:
            return True
    return False


def containsDuplicate2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    left = 0
    while left < len(nums) - 1:
        if nums[left] == nums[left + 1]:
            return True
        left += 1
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(containsDuplicate1(nums))
    print(containsDuplicate2(nums))

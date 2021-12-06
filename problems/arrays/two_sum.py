"""
Two Sum

Link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and integer target, return the indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]

Solution:
Time Complexity: worst case; brute force O(n^2)
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    """
    seen = {}
    for idx in range(len(nums)):
        if target - nums[idx] in seen:
            return [seen[target - nums[idx]], idx]
        seen[nums[idx]] = idx
    return []


def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int

    Approach: using two pointers
    Time complexity: O(n)
    """
    left_pointer = 0
    right_pointer = len(nums) - 1
    while left_pointer <= right_pointer:
        # compute sum of current left and right pointers
        curSum = nums[right_pointer] + nums[left_pointer]
        # if sum is greater than target, move right pointer left
        if curSum > target:
            right_pointer -= 1
        # if sum is less than target, move left pointer right
        if curSum < target:
            left_pointer += 1
        # if sum is equal to target, return results
        else:
            return [left_pointer + 1, right_pointer + 1]
    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    nums = [3, 2, 4]
    target = 6
    print(twoSum(nums, target))
    print(twoSum2(nums, target))

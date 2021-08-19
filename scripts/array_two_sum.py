"""
Two Sum

Link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and integer target, return the indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]
```
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    """
    seen = {}
    for i in range(0, len(nums)):
        if target - nums[i] in seen:
            return (seen[target - nums[i]], i)
        else:
            seen[nums[i]] = i
    return seen


nums = [2, 7, 11, 15]
target = 9
twoSum(nums, target)

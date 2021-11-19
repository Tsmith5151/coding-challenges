""" 
permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Reference: https://leetcode.com/problems/permutations/

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]

    Solution: backtracking
    References:
            https://www.youtube.com/watch?v=kyLxTdsT8ws
            https://www.youtube.com/watch?v=s7AvT7cGdSo
    """
    results = []

    # base base
    if len(nums) == 1:
        return [nums.copy()]
    # apply backtracking
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        for perm in perms:
            perm.append(n)
        results.extend(perms)
        nums.append(n)
    return results


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute(nums))

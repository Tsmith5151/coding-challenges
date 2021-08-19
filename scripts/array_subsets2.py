"""
Subsets II

Reference: https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.	

Example:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""


def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    output = [[]]
    for n in nums:
        output += [curr + [n] for curr in output]

    # get unique pairs
    unique = set([tuple(i) for i in output])
    return [list(i) for i in unique]


if __name__ == "__main__":
    nums = [4, 4, 4, 1, 4]
    print(subsetsWithDup(nums))

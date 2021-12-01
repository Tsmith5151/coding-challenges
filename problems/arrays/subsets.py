"""
Subsets

Link: https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example: 
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Solutions: Cascading approach
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """Solution 1: Cascading approach"""
    output = [[]]
    for n in nums:
        output += [curr + [n] for curr in output]
    return output


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(subsets(nums))

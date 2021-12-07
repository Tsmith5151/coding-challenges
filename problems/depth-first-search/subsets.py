"""
Subsets

Link: https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets
(the power set). 

The solution set must not contain duplicate subsets. Return the solution in any
order. 

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Solutions: DFS
Time Complexity: O(n * 2^n)
"""

from typing import List


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    results = []
    subset = []

    def dfs(i):
        """Depth First Search Helper Function"""
        # base case
        if i >= len(nums):
            results.append(subset.copy())
            return

        # recursive case
        # Left side of tree: decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)  # run dfs on the next element

        # decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)  # empty subset passed to this dfs

    dfs(i=0)
    return results


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(subsets(nums))

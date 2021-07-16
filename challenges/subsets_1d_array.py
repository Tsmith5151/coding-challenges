from typing import List
"""
## Subsets

Link: https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```
"""

# Cascading approach
def subsets(nums: List[int]) -> List[List[int]]:
    output = [[]]
    for n in nums:
        output += [curr + [n] for curr in output]
    return output

subsets([1,2,3])
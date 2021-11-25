"""
Subarray Sum Equals K

Reference: https://leetcode.com/problems/subarray-sum-equals-k/

Given an integer array nums, find the contiguous subarrays where the sum equals k

```
Input: [1,1,1]
k = 2
Output = [1,1], [1,1]
```
"""
from typing import List


def sumKsubArray(nums: List[int], k: int):
    """ " O(N^2) space complexity"""
    results = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub = nums[i : j + 1]
            if sum(sub) == k:
                results.append(sub)
    return results


if __name__ == "__main__":
    print(sumKsubArray([1, 1, 1], k=2))

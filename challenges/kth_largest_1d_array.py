"""
## Kth Largest Value in Array

Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```
"""

def findKthLargest(nums,k):
    nums.sort()
    nums[len(nums)-k]

nums = [3,2,3,1,2,4,5,5,6]
k = 4

findKthLargest(nums,k)
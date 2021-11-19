"""
Kth Largest Value in Array

Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```
"""

# O(log(n))
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort()
    nums[len(nums) - k]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest(nums, k))

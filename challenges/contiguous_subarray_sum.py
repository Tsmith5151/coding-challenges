"""
## Max Contiguous Subarray Sum

Link: https://leetcode.com/problems/maximum-subarray/


Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Note:** Solution below is a brute force implementation with O(n^2)
complexity.
"""

def maxSubArray_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    myList = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            myList.append(sum(nums[i : j + 1]))
    return max(myList)

maxSubArray_1([-2,1,-3,4,-1,2,1,-5,4])
"""
## Two Sum

Link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and integer target, return the indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]
```
"""

# Alternative solution
def shuffle1(nums, n):
    """
    :type nums: List[int]
    :type n: inta
    """
    myList = []
    for i in list(zip(nums[:n],nums[n:])):
        myList.extend(i)
    return myList

def shuffle2(nums, n):
    """
    :type nums: List[int]
    :type n: int
    """
    myList = []
    for idx in range(len(nums)):
        if idx < n:
            myList.append(nums[idx])
            myList.append(nums[idx + n])
        else:
            return myList
        
shuffle1([2,5,1,3,4,7],n=3)
shuffle2([2,5,1,3,4,7],n=3)
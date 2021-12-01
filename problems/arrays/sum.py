"""
Running Sum of 1d Array

Reference: https://leetcode.com/problems/running-sum-of-1d-array/

Given an array nums. We define a running sum of an array as runningSum[i] =
sum(nums[0]…nums[i]). Return the running sum of nums. 

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""


def runningSum(nums):
    """
    :type nums: List[int]
    """
    myList = []
    tmp = 0
    for i in range(len(nums)):
        tmp += nums[i]
        myList.append(tmp)
    return myList


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(runningSum(nums))

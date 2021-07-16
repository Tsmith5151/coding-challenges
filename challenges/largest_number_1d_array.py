"""
Return the largest number in an array that’s less than a given number.
"""

def largestNumber(nums,k):
    nums = sorted(nums)
    return nums[k - 1]
    
nums = [2,5,7,3,2,1]
k = 3
answer = 2

largestNumber(nums,k)
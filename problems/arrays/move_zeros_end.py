""" 
Move Zeros

Reference: https://leetcode.com/problems/move-zeroes

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements. 

Note that you must do this in-place without making a copy of the array.
 
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Time complexity = O(n)
"""


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = 0
    n = len(nums)
    zeros = 0
    while i < n - zeros:
        if nums[i] == 0:  # if num is zero
            nums.insert(n, 0)  # move it to the back
            del nums[i]  # remove from current index
            zeros += 1  # add a zero to help define loop break
        else:
            i += 1  # nonzero, so move pointer along by 1
    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(moveZeroes(nums))

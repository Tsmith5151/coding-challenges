""" 
Move Zeroes

Reference: https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Solution1: Arrays; but requires extra space
Time Complexity: O(2*n)

Solution2: pointers - in-place
Time Complexity: O(n)
"""


def moveZeroes1(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    return [i for i in nums if i != 0] + [i for i in nums if i == 0]


def moveZeroes2(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    left, right = 0, 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            right += 1
            left += 1
        else:
            right += 1
    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    # nums = [2, 1]
    # print(moveZeroes1(nums))
    print(moveZeroes2(nums))

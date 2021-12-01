"""
Sorting Colors

Reference: https://leetcode.com/problems/sort-colors/
        
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
 
Examples:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example:
Input: nums = [2,0,1]
Output: [0,1,2]
"""


def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    red, white, blue = 0, 0, 0
    for i in nums:
        if i == 0:
            red += 1
        elif i == 1:
            white += 1
        elif i == 2:
            blue += 1

    nums[:] = [0] * red + [1] * white + [2] * blue
    return nums


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(sortColors(nums))

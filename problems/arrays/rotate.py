"""
Rotate Array

Reference: https://leetcode.com/problems/rotate-array/ 

Given an array, rotate the array to the right by k steps, where k is
non-negative. 

Example:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Solution:
Time Complexity: O(n) -> Modify in place
Memory Complexity: O(1)

Note: 

k = 2 
x = [1,2,3,4,5]

|  |  | 1 | 2 | 3 | 

when moving an element to the right and it's outside the length of the
array (e.g. 4 & 5), we can use (i + k) % len(nums) to position the element at
the correct index. 

Example: i = 4; (3 + 2) % 5 = index = 0
Example: i = 5; (4 + 2) % 5 = index = 1
"""


def _rotate(nums, left, right):
    """Helper function to rotate array"""
    # reverse the array
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1
    return nums


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    # if k > len of array ---> in case k > len(array)
    k = k % len(nums)

    # initial rotation of the input array
    l, r = 0, len(nums) - 1
    nums = _rotate(nums, l, r)

    # rotate first k elements
    l, r = 0, k - 1
    nums = _rotate(nums, l, r)

    # rotate last k elements
    l, r = k, len(nums) - 1
    nums = _rotate(nums, l, r)
    return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Input:", nums)
    print("Output:", rotate(nums, k))

""" 
Find Minimum in Rotated Sorted Array

Reference: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

"""


def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums is None:
        return []

    results = nums[0]
    left, right = 0, len(nums) - 1

    while left <= right:

        # if we get to a subarray that is already sorted
        if nums[left] <= nums[right]:
            results = min(results, nums[left])
            break

        # Find midpoint
        mid = (left + right) // 2

        # Keep track of smallest value
        results = min(results, nums[mid])

        # if the mid > left pointer value; then we want to search to the right
        # since this portion of the array will have the smallest numbers.
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1

    return results


if __name__ == "__main__":
    nums = [3, 4, 5, 1, 2]
    print(findMin(nums))

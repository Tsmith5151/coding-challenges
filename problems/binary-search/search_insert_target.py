"""
Search Insert Position

Link: https://leetcode.com/problems/search-insert-position/
 
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Solution: Binary Search
Time Complexity: O(logn)

"""


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Search left side
        if target < nums[mid]:
            right = mid - 1

        # Search right side
        if target > nums[mid]:
            left = mid + 1

    # if we cannot find the target in the array:
    return left


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    print(searchInsert(nums, target))

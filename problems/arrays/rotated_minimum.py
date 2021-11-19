""" 
Find Minimum in Rotated Sorted Array

# Reference: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.  [0,1,2,4,5,6,7] if it was rotated 7
times.  Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time
results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum
element of this array.

You must write an algorithm that runs in O(log n) time.

 """


def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int

    Reference: https://www.youtube.com/watch?v=nIVW4P8b1VA

    Solution: modified binary search with complexity O(log n).
    """
    results = nums[0]
    left = 0
    right = len(nums) - 1
    while left <= right:

        # if input array is sorted
        if nums[left] < nums[right]:
            results = min(results, nums[left])
            break

        # Compute midpoint
        mid = (left + right) // 2
        results = min(results, nums[mid])

        # if midpoint is apart of the left sorted portion:
        if nums[mid] >= nums[left]:
            # search the right side of the array
            left = mid + 1

        # if midpoint is apart of the right sorted portion:
        if nums[mid] <= nums[left]:
            right = mid - 1

    return results


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(findMin(nums))

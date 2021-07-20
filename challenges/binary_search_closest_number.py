"""
Given an array of sorted integers, determine
the closest value to a given number


input: [1,2,4,5,6,6,8,9]
target: 11
output = 9

"""
from typing import List


def naive(nums: List[int], target: int):
    """O(n) approach"""
    diff = []
    for i in nums:
        diff.append(abs(target - i))
    return nums[diff.index(min(diff))]


def binary_search(nums: List[int], target: int):
    """Binary search implementation"""
    min_diff = float("inf")  # placeholder to keep track of min number seen
    left = 0
    right = len(nums)
    closest = None
    while left <= right:
        mid = (left + right) // 2

        # ensure we don't go beyond elements of list
        if mid > 0:
            mid_left_diff = abs(target - nums[mid - 1])

        if mid + 1 < len(nums):
            mid_right_diff = abs(target - nums[mid + 1])

        # check if absolute value between left/right are smaller than any seen prior
        if mid_left_diff < min_diff:
            min_diff = mid_left_diff
            closest = nums[mid - 1]

        if mid_right_diff < min_diff:
            min_diff = mid_right_diff
            closest = nums[mid + 1]

        # move the mid point accordingly as in binary search
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

        # if element is the target itself, return number itself
        else:
            return nums[mid]

    return closest


if __name__ == "__main__":

    nums = [1, 2, 4, 5, 6, 6, 8, 9]
    target = 11
    print(naive(nums, target))
    print(binary_search(nums, target))

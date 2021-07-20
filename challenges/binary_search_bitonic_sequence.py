"""
Find the highest number in a bitonic sequence. 

Example of bitonic sequence:
X = [1,2,3,4,5,1,2,3]; peak = 5
Y = [1,6,5,4,3,2,1]; peak = 6
"""

from typing import List


def binary_search(nums: List[int]) -> bool:
    """Return the max value in bitonic sequence"""
    left = 0
    right = len(nums) - 1

    # requires at least length of 3
    if len(nums) < 3:
        return None

    while left <= right:
        mid = (left + right) // 2

        # check both left and right sides; account for edge case
        mid_left = nums[mid - 1] if mid - 1 < 0 else float("-inf")
        mid_right = nums[mid + 1] if mid + 1 > 0 else float("inf")

        # check conditions for left side
        if mid_left < nums[mid] and mid_right > nums[mid]:
            left = mid + 1

        # check conditions for right side
        elif mid_left > nums[mid] and mid_right < nums[mid]:
            right = mid - 1

        elif mid_left < nums[mid] and mid_right < nums[mid]:
            return nums[mid]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    print(binary_search(nums))

"""
Given an array of integers nums sorted in ascending order, check
if target value is a duplicated value or not. 

time complexity - O(N)
"""

from typing import List


def is_duplicate(nums: List[int], target: int):
    """Check if input target is a duplicate"""
    if target in nums:
        counter = {i: nums.count(i) for i in nums}
        if counter[target] >= 1:
            return True


if __name__ == "__main__":
    print(is_duplicate([1, 4, 5, 5], 5))

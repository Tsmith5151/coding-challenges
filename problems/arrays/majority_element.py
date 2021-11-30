""" 
Majority Element

Reference: https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

from typing import DefaultDict


def majorityElement(nums):
    """
    :type nums: ListaultDict(int)ist[int]
    :rtype: int
    """
    count = DefaultDict(int)
    results, max_count = 0, 0

    for i in nums:
        count[i] += 1

        # keep track of max value
        results = i if count[i] > max_count else results

        # keep track of value with max count
        max_count = max(count[i], max_count)

    return results


if __name__ == "__main__":
    nums = [3, 2, 3]
    print(majorityElement(nums))

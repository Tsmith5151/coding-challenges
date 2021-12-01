"""
Single Number

Reference: https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for
one. Find that single one. Note: Your algorithm should have a linear runtime
complexity. Could you implement it without using extra memory? 

Input: [2,2,1]
Output: 1
"""

from collections import defaultdict


def singleNumber(nums, results=[]):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Create Default Dictionary
    n_dict = defaultdict(list)
    for n in nums:
        n_dict[n].append(n)

    # Identify the non-dups from dictionary
    non_dup = [v[0] for k, v in n_dict.items() if len(v) == 1][0]
    return non_dup


if __name__ == "__main__":
    nums = [2, 2, 1]
    print(singleNumber(nums))

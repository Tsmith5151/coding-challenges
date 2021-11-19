""" 
Count nice pairs in an array.

Reference: 

You are given an array nums that consists of non-negative integers. Let us
define rev(x) as the reverse of the non-negative integer x. For example,
rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it
satisfies all of the following conditions:

- 0 <= i < j < nums.length 
- nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) i

Return the number of nice pairs of indices. Since that number can be too large, return
it modulo 109 + 7.

Example 1:

Input: nums = [42,11,1,97]
Output: 2

Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

Example 2:

Input: nums = [13,10,35,24,76]
Output: 4

Time Complexity: O(N)
Space Complexity: O(N)
"""
import collections


def countNicePairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    def rev(x):
        """Reverse String"""
        return int(str(x)[::-1])

    MOD = 10 ** 9 + 7
    total = 0
    c = collections.Counter()
    for x in nums:
        current = x - rev(x)
        total += c[current]
        total %= MOD
        c[current] += 1
    return total % MOD


if __name__ == "__main__":
    nums = [42, 11, 1, 97]
    print(countNicePairs(nums))
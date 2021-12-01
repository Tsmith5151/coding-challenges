""" 
Missing Number

Reference: https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in the range [0, n], return
the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity
and O(n) runtime complexity? 

Input: nums = [9,6,4,2,3,5,7,0,1] Output: 8 Explanation: n = 9 since there are 9
numbers, so all numbers are in the range [0,9]. 8 is the missing number in the
range since it does not appear in nums. 
"""


def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int

    Time complexity: O(n)
    """
    return sum(range(len(nums) + 1)) - sum(nums)


if __name__ == "__main__":
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(missingNumber(nums))

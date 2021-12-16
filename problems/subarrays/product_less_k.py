""" 
Subarray Product Less Than K
 
Reference:  https://leetcode.com/problems/subarray-product-less-than-k/

Given an array of integers nums and an integer k, return the number of
contiguous subarrays where the product of all the elements in the subarray is
strictly less than k. 

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0

Solution: we can do this brute force, but that is O(n^2).
Time Complexity: O(n)

[10,5,2,6] < 100
"""


def numSubarrayProductLessThanK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    max_prod = nums[0]  # optimize for maximum product
    cur_product = 0
    for i in range(len(nums) - 1):
        cur_product *= nums[i]
        max_prod = max(max_prod, cur_product)
    return max_prod


if __name__ == "__main__":
    nums = [10, 5, 2, 6]
    k = 100
    print(numSubarrayProductLessThanK(nums, k))

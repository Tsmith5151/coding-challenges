""" 
Partition to K Equal Sum Subsets

Reference: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/


Given an integer array nums and an integer k, return true if it is possible to
divide this array into k non-empty subsets whose sums are all equal. 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false

Solution: Backtracking
Time Complexity: O(k^n); k = k number of decisions, n = size of array

Slightly more efficient solution:
Time Complexity: O(k * 2^n); height of tree = n; k = k number of decisions (2);
so we have to find "k" number of subsets. In the next k subsets, we can't reuse
the numbers that was used in previous k subsets.
We determine if we include the number in our sum or not.

Reference: https://www.youtube.com/watch?v=mBk4I0X46oI 
"""


def canPartitionKSubsets(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    target = sum(nums) // k
    used = [False] * len(nums)

    def backtracking(index, k_partitions, cur_sum):
        # base case
        if k == 0:  # no more subsets
            return True
        if cur_sum == target:
            # build next subset
            return backtracking(index, k_partitions - 1, 0)

        # Recursive calls
        # Iterate over remaining values in nums
        for j in range(index, len(nums)):

            # Two decisions: use the value or not
            # Cannot use if we already used it
            # and we do not exceed the target value
            if used[j] and cur_sum + nums[j] > target:
                continue  # can skip since not a valid subset

            # If we use it, mark it as used
            used[j] = True

            # Recursive call
            if backtracking(j + 1, k_partitions, cur_sum + nums[j]):
                return True  # found a valid way

            # Clean up -> we are no longer using the value
            used[j] = False

        return False  # no valid subset

    # call backtracking
    return backtracking(0, k, 0)


if __name__ == "__main__":
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(canPartitionKSubsets(nums, k))

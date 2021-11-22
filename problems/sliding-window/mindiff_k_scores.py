""" 
Minimum Difference Between Highest and Lowest of K Scores

Reference: https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.

Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.

Solution: Sliding-Window
Time Complexity: O(nlogn)
Sort input array and then take difference between score of nums[i] and nums[i +
window]. 
"""


def minimumDifference(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort()
    left, right = 0, k - 1
    diff = float("inf")

    while right < len(nums):
        diff = min(nums[right] - nums[left], diff)
        left += 1
        right += 1

    return diff


if __name__ == "__main__":
    nums = [9, 4, 1, 7]  # [1,4,7,9]
    k = 2
    print(minimumDifference(nums, k))

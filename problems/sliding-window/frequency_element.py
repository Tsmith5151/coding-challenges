""" 
Frequency of the Most Frequent Element

https://leetcode.com/problems/frequency-of-the-most-frequent-element/

The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two
times to make nums = [4,4,4]. 
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1


Solution: Sort + Sliding Window
Time Complexity: O(n log n)
Equation for the frequency of an element: nums[right] * len(window) < total + k

Reference: https://www.youtube.com/watch?v=vgBrQ0NM5vE
"""


def maxFrequency(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    total = 0
    left, right = 0, 0
    results = 0

    while right < len(nums):
        total += nums[right]
        # while the window is invalid
        while nums[right] * (right - left + 1) > total + k:
            total -= nums[left]
            # shrink window size
            left += 1
        results = max(results, right - left + 1)
        right += 1
        # window is valid -> expand window
        right += 1
    return results


if __name__ == "__main__":
    nums = [1, 2, 4]
    k = 5
    print(maxFrequency(nums, k))

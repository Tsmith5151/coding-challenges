""" 
K-sum Pairs in an Array
 
Reference: https://leetcode.com/problems/k-sum-pairs-in-an-array/

Given an array of integers nums and an integer k, return the number of unique k-sum pairs in the array.

A k-sum pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-sum pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-sum pairs in the array, (1, 2), (2, 3), (3, 4)
and (4, 5).

Solution: two pointers
Time complexity: O(n)
"""


def findPairs(nums, k):
    """
    :type nums: List[int]
    :type k: int

    Approach: using two pointers
    Time complexity: O(nlogn)
    """
    nums = list(set(nums))
    nums.sort()
    results = []
    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer <= right_pointer:
        # compute sum of current left and right pointers
        curDiff = abs(nums[right_pointer] - nums[left_pointer])
        # if diff is less than target, move right pointer left
        if curDiff < k:
            right_pointer += 1
        # if diff is greater than target, move left pointer right
        if curDiff > k:
            left_pointer += 1
        # if diff is equal to target, return results
        else:
            results.append([left_pointer + 1, right_pointer + 1])
    return results


if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5]
    k = 2
    print(findPairs(nums, k))

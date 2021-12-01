"""
Subarray Sum Equals K

Reference: https://leetcode.com/problems/subarray-sum-equals-k/

Given an integer array nums, find the contiguous subarrays where the sum equals k

Input: [1,1,1]
k = 2
Output = [1,1], [1,1]

Solution: the brute force approach checks each subarray and determines if the
sum equals K. Alternatively, we can create a hash map where the key is the
prefix sum and the count is the value.  
Time Complexity: The brute force approach is O(n^2). We can do better: O(n).

Reference: https://www.youtube.com/watch?v=fFVZt-6sgyo&t=18s
"""


def sumKsubArray1(nums, k):
    """
    Brute Force Approach
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    results = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub = nums[i : j + 1]
            if sum(sub) == k:
                results.append(sub)
    return results


def sumKsubArray2(nums, k):
    """
    Hashp Map Approach
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # TODO
    return


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(sumKsubArray1(nums, k))

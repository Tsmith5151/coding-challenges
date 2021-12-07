"""
Subarray Sum Equals K

Reference: https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.


Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Solution: the brute force approach checks each subarray and determines if the
sum equals K. Alternatively, we can create a hash map where the key is the
prefix sum and the count is the value.  
Time Complexity: The brute force approach is O(n^2). 

We can do better by using a hash map "O(n)". They keys are the prefix sums and
the values is the count of the number of times the prefix sum occurs. We can
remove a prefix from an array such that sum of the subarray is equal to k (sum
- k). 

Also, since there can be negative values in the input array, we are
keeping track of the count for each prefix, because there can be multiple
prefixes that sum to 'n'. 

Reference: https://www.youtube.com/watch?v=fFVZt-6sgyo&t=18s
"""


def subarraySum1(nums, k):
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
    return len(results)


def subarraySum2(nums, k):
    """
    Hash Map Approach
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    results = 0
    prefixSums = {0: 1}
    curSum = 0

    for num in nums:
        curSum += num

        # if we can find a prefix sum with size "diff";
        # then can find potential results;
        # we can have multiple prefix sums that add up to diff
        diff = curSum - k

        # get prefix sums that add up to diff
        # if not exists; will return 0
        results += prefixSums.get(diff, 0)

        # add the prefix sum the current sum computed
        # incrementing the number of prefix sums that has this particular sum
        prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

    return results


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(subarraySum1(nums, k))
    print(subarraySum2(nums, k))

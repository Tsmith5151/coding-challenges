"""
Kth Largest Value in Array

Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Solution: Min Heap
Time Complexity: O(logn)
"""

import heapq


def findKthLargest2(nums, k):
    """
    Using min heap to find kth largest
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    heap = []
    heapq.heapify(heap)
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            # pop the smallest element
            heapq.heappop(heap)
    # pop smallest element (e.g. will be len(2)) to return largest value
    return heapq.heappop(heap)


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(findKthLargest2(nums, k))

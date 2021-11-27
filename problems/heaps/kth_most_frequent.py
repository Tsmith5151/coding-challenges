""" 
Top K Most Frequent Elements

Reference: https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 
Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Solution1: Counter
Time Complexity: O(n)

Solution2: Max Heap
Time Complexity: O(nlogk); where n = len(nums) and k = k.
"""


def topKFrequent1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    count = {}
    # create a list where the size of the list = len(nums)
    # we are to store the frequency of each value in index of the list.
    frequency = [[] for i in range(len(nums) + 1)]

    # populate the counter dictionary
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    # update the freq of each value in the frequency list
    for num, freq in count.items():
        frequency[freq].append(num)

    results = []
    for i in range(len(frequency) - 1, 0, -1):
        if frequency[i] != [] and k > 0:
            results.append(frequency[i][0])
            k -= 1
    return results


import heapq


def topKFrequent2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    count = {}
    # populate the counter dictionary
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    # create a heap; store negative frequency of each value to create min heap
    minheap = []
    for num, freq in count.items():
        heapq.heappush(minheap, (-freq, num))

    return [heapq.heappop(minheap)[1] for i in range(0, k)]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print("Solution 1:", topKFrequent1(nums, k))
    print("Solution 2:", topKFrequent2(nums, k))

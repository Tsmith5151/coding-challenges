from typing import List
from collections import defaultdict


def merge(intervals: List[List[int]]):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    
    results = []
    intervals.sort()
    if intervals == []:
        return []
    
    for interval in intervals:
        if results == []:
            results.append(interval)
        elif interval[0] <= results[-1][1]:
            results[-1] = [results[-1][0],max(results[-1][1],interval[1])]
        else:
            results.append(interval)
    return results


def runningSum(nums):
    """
    :type nums: List[int]
    """
    myList = []
    tmp = 0
    for i in range(len(nums)):
        tmp += nums[i]
        myList.append(tmp)
    return myList


def singleNumber(nums, results=[]):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Create Default Dictionary
    n_dict = defaultdict(list)
    for n in nums:
        n_dict[n].append(n)

    # Identify the non-dups from dicitonary
    non_dup = [v[0] for k, v in n_dict.items() if len(v) == 1][0]
    return non_dup


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    """
    seen = {}
    for i in range(0, len(nums)):
        if target - nums[i] in seen:
            return (seen[target - nums[i]], i)
        else:
            seen[nums[i]] = i
    return seen


def maxSubArray_1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    myList = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            myList.append(sum(nums[i : j + 1]))
    return max(myList)


def maxSubArray_2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current_sum = global_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], nums[i] + current_sum)
        global_sum = max(current_sum, global_sum)
    return global_sum


def _shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    """
    myList = []
    for idx in range(len(nums)):
        if idx < n:
            myList.append(nums[idx])
            myList.append(nums[idx + n])
        else:
            return myList


def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    myList = []
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] == nums[j] and i < j:
                myList.append([i, j])
    return len(myList)


def smallerNumbersThanCurrent(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    myList = []
    for i in range(len(nums)):
        myList.append(len([1 for j in range(len(nums)) if nums[j] < nums[i]]))
    return myList


def finalPrices(prices):
    """
    :type prices: List[int]
    :rtype: List[int]
    """
    myList = []
    for i in range(len(prices) - 1):
        for j in prices[i + 1 :]:
            if prices[i] >= j:
                price = prices[i] - j
                break
            else:
                price = prices[i]
        myList.append(price)
    return myList + prices[-1:]


def busyStudent(startTime, endTime, queryTime):
    """
    :type startTime: List[int]
    :type endTime: List[int]
    :type queryTime: int
    :rtype: int
    """
    return sum(
        [
            1 if queryTime >= startTime[i] and queryTime <= endTime[i] else 0
            for i in range(len(startTime))
        ]
    )

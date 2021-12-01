"""
Merge Intervals

Reference: https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from typing import List


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
            results[-1] = [results[-1][0], max(results[-1][1], interval[1])]
        else:
            results.append(interval)
    return results


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))

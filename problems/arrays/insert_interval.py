""" 
Insert Interval

Reference: https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals where intervals[i]
= [starti, endi] represent the start and the end of the ith interval and
intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another
interval.

Insert newInterval into intervals such that intervals is still sorted in
ascending order by starti and intervals still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Solution: pointers 
Reference: https://www.youtube.com/watch?v=A8NUOmlwOlM
"""


def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    output = []
    pointer = 0
    # keep track of pointer to the start of the new interval
    for start, end in intervals:
        if start < newInterval[0]:
            output.append([start, end])
            pointer += 1
        else:
            break

    # insert or merge our new interval
    if not output or output[-1][1] < newInterval[0]:
        output.append(newInterval)
    else:
        # append:
        output[-1][1] = max(output[-1][1], newInterval[1])

    # insert or merge all the remaining intervals
    for start, end in intervals[pointer:]:
        if output[-1][1] < start:
            output.append([start, end])
        else:
            output[-1][1] = max(output[-1][1], end)
    return output


if __name__ == "__main__":
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(insert(intervals, newInterval))

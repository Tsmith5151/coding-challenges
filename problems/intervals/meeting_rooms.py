""" 
Minimum Meeting Rooms 

Reference: https://www.lintcode.com/problem/919/


Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

In other words, find the maximum number of non-overlapping meetings at any
point in time.

Example

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room

time complexity: O(nlogn)

Example diagram:
# 0======================30
# 	5====15
# 		 15=======25

Rearrange as: 
start = 0,5,15
end = 10,20,30 
"""


def minMeetingRooms(intervals):
    """
    :type intervals: List[int]
    :rtype: int
    """

    # sort intervals for start/end time
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])
    results, counter = 0, 0
    s = 0
    e = 0

    # loop through intervals until end of array
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            counter += 1
        else:
            # move pointer of end time
            e += 1
            counter -= 1  # end of meeting
        results = max(results, counter)  # max available rooms
    return results


if __name__ == "__main__":
    intervals = [(0, 30), (5, 10), (15, 20)]
    print(minMeetingRooms(intervals))

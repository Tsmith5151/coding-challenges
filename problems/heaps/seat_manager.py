""" 
Seat Reservation Manager

Reference: https://leetcode.com/problems/seat-reservation-manager/

Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n): Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
int reserve(): Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber): Unreserves the seat with the given seatNumber.


Example 1:

Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();  All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();  The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();  The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();  The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();  The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();  The only available seat is seat 5, so return 5.
seatManager.unreserve(5); Unreserve seat 5, so now the available seats are [5].

Solution: 
1 Min Heap -> keep tracks of the unreserved seats; continuously pop the minimum
from the min heap. 

Time Complexity = O(log n)
"""

import heapq


class SeatManager:
    def __init__(self, n):
        self.n = n
        self.unreserved = [i for i in range(1, n + 1)]

    def reserve(self):
        """
        Fetches the smallest-numbered unreserved seat, reserves it, and
        returns its number.

        This method only gets called when seats are available.
        """

        # pop the minimum from the min heap
        return heapq.heappop(self.unreserved)

    def unreserve(self, seatNumber):
        """
        Unreserved the seat with the given seatNumber.

        This method only gets called when seats that already reserved.
        """
        heapq.heappush(self.unreserved, seatNumber)


if __name__ == "__main__":
    input = [
        "SeatsManager",
        "reserve",
        "reserve",
        "unreserve",
        "reserve",
        "reserve",
        "reserve",
        "reserve",
        "unreserve",
    ]
    seats = [[5], [], [], [2], [], [], [], [], [5]]
    m = SeatManager(5)
    m.reserve()
    m.reserve()
    m.unreserved(1)

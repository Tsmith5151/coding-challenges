""" 
Cheapest Flights Within K Stops

Reference:
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
marked blue in the picture.


Solution: Bellman-Ford algorithm (shortest path with at most k stops)  
Time Complexity: O(E * K); E = number of edges, K = number of stops. For each loop (e.g. k stops), we will visit all edge. 

            City 0
            /     \
           /       \
   100    /         \    500
         /           \
    City 1 - - - - - City 2 
              100  

Each edge = Flight that connects two cities and associated price. 
What is the cheapest way to fly from city 0 to city 2 with at most
'k' stops?

Start at city 0 -> apply BFS 
 
Reference: https://www.youtube.com/watch?v=5eIK3zUdYmE&t=451s
"""


def findCheapestPrice(n, flights, src, dst, k):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type k: int
    :rtype: int
    """

    def bfs(prices):
        """Breath First Search Helper Function"""
        temp = prices.copy()
        # iterate through all edges
        for source, dest, price in flights:
            # skip if source node is infinity
            if prices[source] == float("inf"):
                continue
            # if we found a new minimum price to reach dest node
            if prices[source] + price < temp[dest]:
                # update the price
                temp[dest] = prices[source] + price
        return temp

    prices = {0: 0, 1: float("inf"), 2: float("inf")}
    for i in range(k + 1):
        prices = bfs(prices)

    # if no path found, return -1
    return -1 if prices[dst] == float("inf") else prices[dst]


if __name__ == "__main__":
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dest = 2
    k = 1
    print(findCheapestPrice(n, flights, src, dest, k))

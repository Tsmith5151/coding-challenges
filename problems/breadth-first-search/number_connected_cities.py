""" 
Number of Provinces
 
Reference: https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Solution: Breadth First Search w/ Queue
Time Complexity: O(n^2)
Memory Complexity: O(n^2)
"""

import collections


def findCircleNum(isConnected):
    """
    :type isConnected: List[List[int]]
    :rtype: int
    """
    n_cities = len(isConnected)
    visited = set()
    counter = 0

    def bfs(city):
        """Breath First Search Helper Function"""
        queue = collections.deque()
        queue.append(city)
        while queue:
            city = queue.popleft()
            for neighbor in range(n_cities):
                # For each city - iterate through all the neighbors
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    # traverse through each city the in matrix
    for city in range(n_cities):
        # check if there is a link between the ith row and the jth column
        if isConnected[city][city] == 1 and city not in visited:
            bfs(city)
            counter += 1
    return counter


if __name__ == "__main__":
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    print(findCircleNum(isConnected))

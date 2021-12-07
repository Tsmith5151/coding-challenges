""" 
Maximal Square

Reference: https://leetcode.com/problems/maximal-square/

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Solution: Recursion (top-down)
Time Complexity: O(m*n)
Memory Complexity: O(m*n)
"""


def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    row, cols = len(matrix), len(matrix[0])
    cache = {}  # map each position (r,c) -> max length of the square

    def dfs(r, c):
        # base case (out of bounds)
        if r >= row or c >= cols:
            return 0
        # check if already computed and stored in cache
        if (r, c) not in cache:

            # compute area
            down = dfs(r + 1, c)
            right = dfs(r, c + 1)
            diagonal = dfs(r + 1, c + 1)

            # initial to zero
            cache[(r, c)] = 0
            if matrix[r][c] == "1":
                # update cache
                cache[(r, c)] = 1 + min(down, right, diagonal)
        else:
            return cache[(r, c)]

    dfs(0, 0)  # start from top left corner
    return max(cache.values()) ** 2


if __name__ == "__main_":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print(maximalSquare(matrix))

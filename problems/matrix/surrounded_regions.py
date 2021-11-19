""" 
Surrounded Regions

Reference: https://leetcode.com/problems/surrounded-regions/

Given an m x n matrix board containing 'X' and 'O', capture all regions that
are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output:
[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation: Surrounded regions should not be on the border, which means that
any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not
on the border and it is not connected to an 'O' on the border will be flipped
to 'X'. Two cells are connected if they are adjacent cells connected
horizontally or vertically.

Solution: DFS
Time Complexity: O(m*n)
"""

# TODO
def solve(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """

    pass


if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    print(solve(board))

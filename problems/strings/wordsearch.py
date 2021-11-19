""" 
Word Search

Reference: https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Solution: Backtracking with DFS
Time Complexity: O(n * m * dfs); dfs = len(word) * 4 ^ len(word); 4^n 
O (n * m * 4^n)

We will look at every cell in the grid and check the neighbors
to see if we can construct the word. 

Reference: https://www.youtube.com/watch?v=pfiQ_PS1g8E&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=1
"""


def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    # get dimensions of grid
    rows, cols = len(board), len(board[0])

    # we cannot revisit the word if we have already visited it
    path = set()

    def dfs(r, c, i):
        # base case -> finish the entire word
        if i == len(word):
            return True
        # base case -> out of bounds in the grid
        # 1.) out of bounds of board
        # 2.) row or col is out bounds
        # 3.) character in word [position i] does not match the character in
        # the grid
        # 4.) we have already visited this cell
        if (
            (r < 0 or c < 0)
            or (r >= rows or c >= cols)
            or (word[i] != board[r][c])
            or ((r, c) in path)
        ):
            return False

        # continue to search
        path.add((r, c))  # found a character in word

        # Run dfs in all 4 adjacent cells; add 1 to i since character in word is found
        res = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )  # return True if we can find the word
        path.remove((r, c))  # clean up path; remove position we just added to path
        return res

    # iterate over every position in the board
    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, i=0):
                return True

    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(exist(board, word))

""" 
Set Matrix Zeroes

Reference: https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Example: 

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Solution:
Time Complexity: O(m*n) 
Memory: O(m+n)
"""


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    # Initialize arrays to mark the rows/columns that need to be set to zero
    row_zeros = []
    col_zeros = []

    # Mark the rows and columns that need to be set to zero
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if matrix[row][col] == 0:
                row_zeros.append(row)
                col_zeros.append(col)

    # Convert rows to all zeros
    for idx in row_zeros:
        matrix[idx] = [0] * len(matrix[0])
    for idx in col_zeros:
        for row in range(0, len(matrix)):
            matrix[row][idx] = 0

    return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(setZeroes(matrix))

"""
Count Negative Numbers in a Sorted Matrix

Reference: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

Example
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
"""


def countNegatives(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    count = 0

    for row in grid:
        if row[-1] >= 0:
            continue
        else:
            count += len(list(filter(lambda x: x < 0, row)))
    return count


sample = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
countNegatives(sample)

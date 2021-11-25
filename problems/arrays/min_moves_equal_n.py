""" 
Minimum Moves to Equal Array Elements

Reference: https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

Given an integer array nums of size n, return the minimum number of moves
required to make all array elements equal. 

In one move, you can increment n - 1 elements of the array by 1.

Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
Example 2:

Input: nums = [1,1,1]
Output: 0
"""


def minMoves(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return sum(nums) - min(nums) * len(nums)


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(minMoves(nums))

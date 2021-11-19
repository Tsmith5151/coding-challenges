"""
Search Insert Position

Link: https://leetcode.com/problems/search-insert-position/
 
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.


You must write an algorithm with O(log n) runtime complexity.	
 
"""


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    return sorted(nums + [target]).index(target)


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    searchInsert(nums, target)

"""
Number of good pairs

Reference: https://leetcode.com/problems/number-of-good-pairs/

Given an array of integers nums. A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

"""


def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    myList = []
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] == nums[j] and i < j:
                myList.append([i, j])
    return len(myList)


if __name__ == "__main__":
    print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))

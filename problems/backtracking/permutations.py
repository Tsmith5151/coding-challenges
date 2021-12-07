""" 
Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Reference: https://leetcode.com/problems/permutations/

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

Example: Each level is a sub-array:

                          [1,2,3]
                        /    |    \
                    [2,3]  [1,3]   [1,2]
                     /  \    /  \    /  \
                   [3] [2] [3] [1] [2]  [1]
                   
Remove value in each sub-array, and then add the value back to each sub-array
after we backtrack.
"""


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]

    Solution: backtracking
    References:
            https://www.youtube.com/watch?v=kyLxTdsT8ws
            https://www.youtube.com/watch?v=s7AvT7cGdSo
    """
    results = []

    # base case: reach end of tree
    # all permutations have been generated (only 1 perm left)
    if len(nums) == 1:
        return [nums.copy()]

    # go thru each value in nums:
    for i in range(len(nums)):

        # pop first value
        n = nums.pop(0)

        # then we get the permutations of the remaining values
        perms = permute(nums)

        # iterate over the perms and add the two permutations:
        # [1,2,3] -> [2,3,1] + [3,2,1]
        for perm in perms:
            perm.append(n)
        results.extend(perms)

        # add the value back to the list
        nums.append(n)
    return results


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute(nums))

""" 
Three Sum

Reference: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k]
== 0. 

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

Solution: Two pointers  
Time complexity: O(nlogn) + O(n^2) = O(n^2)
Space complexity: O(1) or O(n)

Reference: https://www.youtube.com/watch?v=jzZsG8n2R9A
"""


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    results = []
    # sort the input array to avoid duplicates
    nums.sort()

    # iterate through the array
    for idx, i in enumerate(nums):
        # to avoid using the same value twice and continue to next iteration
        if idx > 0 and i == nums[idx - 1]:
            continue
        # apply two sum approach: set the left and right pointers
        left = idx + 1
        right = len(nums) - 1
        while left < right:
            threeSum = i + nums[left] + nums[right]
            # threshold is target 0
            if threeSum > 0:
                right -= 1
            # threshold target
            elif threeSum < 0:
                left += 1
            # if the sum is 0, add to results
            else:
                results.append([i, nums[left], nums[right]])
                left += 1
                # update the left most pointer now
                # update the left and check if the value is the same
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return results


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))

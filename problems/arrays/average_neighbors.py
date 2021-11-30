""" 
Array With Elements Not Equal to Average of Neighbors

Reference:
https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

You are given a 0-indexed array nums of distinct integers. You want to rearrange
the elements in the array such that every element in the rearranged array is not
equal to the average of its neighbors.

More formally, the rearranged array should have the property such that for every
i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not
equal to nums[i].

Return any rearrangement of nums that meets the requirements.

Example 1:

Input: nums = [1,2,3,4,5]
Output: [1,2,4,5,3]
Explanation:
When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.

Solution: two pointers
Time complexity: O(nlogn) -> note we have to sort the input array. 
Reference: https://www.youtube.com/watch?v=Wmb3YdVYfqM    
"""


def rearrangeArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    nums.sort()
    results = []
    left, right = 0, len(nums) - 1
    while len(results) != len(nums):
        results.append(nums[left])
        left += 1
        if left < right:
            results.append(nums[right])
            right -= 1
    return results


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(rearrangeArray(nums))

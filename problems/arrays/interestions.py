"""
Intersection of Two Arrays II

Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note: Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.


Solution 1: Use a defaultdict
Time Complexity: O(n*m)

Solution 2: Use a counter 
Time Complexity: O(n)

Solution 3: Two pointers
Time Complexity: O(n + m)
"""

from collections import defaultdict, Counter


def intersection1(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    if not nums1 or not nums2:
        return []

    _min = min(nums1, nums2)
    _max = max(nums1, nums2)

    counter = defaultdict(int)
    for i in range(0, len(_min)):
        counter[_min[i]] = 1

    for i in range(0, len(_max)):
        if _max[i] in counter:
            counter[_max[i]] += 1

    return [k for k, v in counter.items() if v > 1]


def intersection2(nums1, nums2):
    """
    type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    if not nums1 or not nums2:
        return []

    # save in a multiset the smallest
    counter = Counter(nums1)

    # find matches, removing from counter when found
    matches = []
    for num in max(nums1, nums2):
        if counter[num] > 0:
            matches.append(num)
            counter[num] -= 1
    return matches


def intersection3(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    intersect = []
    left1, left2 = 0, 0
    while left1 < len(nums1) and left2 < len(nums2):
        # cases where interesect
        if nums1[left1] == nums2[left2] or left1 == 0:  # add edge case at the end
            if nums1[left1] != nums1[left1 - 1]:
                intersect.append(nums1[left1])
            left1 += 1
            left2 += 1

        # sorted arrays -> so move left1 up if less than left2
        elif nums1[left1] < nums1[left2]:
            left1 += 1
        else:
            left2 += 1
    return intersect


if __name__ == "__main__":
    nums1 = [2, 3, 3, 5, 6, 11]
    nums2 = [3, 3, 7, 15, 31]

    print(intersection1(nums1, nums2))
    print(intersection2(nums1, nums2))
    print(intersection3(nums1, nums2))

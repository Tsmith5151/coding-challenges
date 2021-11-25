""" 
Permutation in String

Reference: https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Solution: Hash map with sliding window
Time Complexity: O(n)
Reference: https://www.youtube.com/watch?v=UbyhOgBN834
"""


from collections import defaultdict


def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """

    # Build hash map
    s1_hash = defaultdict(int)
    for i in range(len(s1)):
        s1_hash[s1[i]] += 1

    # Add pointers
    left_pointer = 0
    right_pointer = len(s1)

    # sliding window:
    while right_pointer <= len(s2):
        # check if s1 is in s2
        s2_hash = defaultdict(int)
        for i in range(left_pointer, right_pointer):
            s2_hash[s2[i]] += 1

        # check if dictionaries are equal
        if s1_hash == s2_hash:
            return True

        # move left pointer
        left_pointer += 1
        right_pointer += 1

    return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    s3 = "eidboaoo"

    s1 = "adc"
    s2 = "dcda"
    print(checkInclusion(s1, s2))
    # print(checkInclusion(s1, s3))

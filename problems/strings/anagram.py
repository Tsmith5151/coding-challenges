""" 
Valid Anagram

Reference: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

Note: an anagram must have the same characters and quantities for each string
to be valid. 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Solution: counter 
Time Complexity : O(s + t)
Memory Complexity : O(s + t)
"""


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[s[i]] = count_t.get(s[i], 0) + 1

    if count_s == count_t:
        return True
    else:
        return False


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))

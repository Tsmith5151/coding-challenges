""" 
Given a string s, return the longest palindromic substring in s.

Reference: https://leetcode.com/problems/longest-palindromic-substring/

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

Solution: iterate through the string and check to the left and right of each
character to see if the substring is a palindrome. 
Time Complexity: O(n^2)

Reference: https://www.youtube.com/watch?v=XYQecbcd6_c
"""


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    results = ""
    results_len = 0
    left, right = 0, 0

    for i in range(len(s)):

        # odd case, like "aba"
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # length of palindrome = right - left + 1
            if (right - left + 1) > results_len:
                results = s[left : right + 1]
                results_len = len(results)
            left -= 1
            right += 1

        # even case, like "abba"
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > results_len:
                results = s[left : right + 1]
                results_len = right - left + 1
            left -= 1
            right += 1
    return results


if __name__ == "__main__":
    s = "cbbd"
    print(longestPalindrome(s))

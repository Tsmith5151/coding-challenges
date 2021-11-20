""" 
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Reference: https://leetcode.com/problems/implement-strstr/

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Explanation: find the first occurrence of "ll" in "hello"

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Solution: nested loop
Time Complexity: O(m*n)
"""


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i : i + len(needle)] == needle:
            return i


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))

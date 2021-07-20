"""
Reverse String

Link: https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```
"""


def reverseString(s):
    """
    :type s: List[str]
    :rtype: List[str]
    """
    return s[::-1]


s = ["h", "e", "l", "l", "o"]
reverseString(s)

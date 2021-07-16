"""
## Palindrome Number

Link: https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```
"""

def isPalindrome(x: int) -> bool:
    return True if str(x)[::-1] == str(x) else False

isPalindrome(121)
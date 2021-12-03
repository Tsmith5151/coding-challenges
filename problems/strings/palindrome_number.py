"""
Palindrome Number

Reference: https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
"""


def isPalindrome1(x):
    """
    :type x: int
    :rtype: bool
    """
    return True if str(x)[::-1] == str(x) else False


def isPalindrome2(x):
    """
    :type x: int
    :rtype: bool
    """
    left = 0
    right = len(x) - 1

    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1


if __name__ == "__main__":
    x = -121
    print(isPalindrome1(x))
    print(isPalindrome1(x))

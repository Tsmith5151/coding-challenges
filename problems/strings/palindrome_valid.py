""" 
Valid Palindrome

Reference: https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Solution: Two pointers
Time Complexity: O(n)
Memory Complexity: O(1)
"""


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    left = 0
    right = len(s) - 1
    while left < right:
        # Skip non-alphanumeric characters
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and right > left:
            right -= 1
        while s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    s = " "
    s = "0P"
    print(isPalindrome(s))

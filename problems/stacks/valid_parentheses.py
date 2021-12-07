"""
Valid Parentheses

Reference: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Solution: Stack
Time Complexity: O(n)
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    mapping = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c in mapping:
            if stack and stack[-1] == mapping[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


if __name__ == "__main__":
    string = "()[]{}"
    print(isValid(string))

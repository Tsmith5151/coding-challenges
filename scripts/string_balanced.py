"""
Split a String in Balanced Strings

Link: https://leetcode.com/problems/split-a-string-in-balanced-strings/

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Example
```
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
```
"""


def balancedStringSplit(s):
    """
    :type s: str
    :rtype: int
    """
    counter, total = 0, 0

    for i in s:
        if i == "R":
            counter += 1
        else:
            counter += -1
        if counter == 0:
            total += 1

    return total


s = "RLRRLLRLRL"
balancedStringSplit(s)

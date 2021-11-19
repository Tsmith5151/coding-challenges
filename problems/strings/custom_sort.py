"""
Custom String Sort

Reference: https://leetcode.com/problems/custom-sort-string/

You are given two strings order and s. All the words of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Example:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
"""
from collections import defaultdict


def customSortString(order, string):
    """
    :type order: str
    :type s: str
    :rtype: str
    """
    look_up = defaultdict(int)
    i = 0
    for c in order:
        look_up[c] = i
        i += 1
    return "".join(sorted(string, key=lambda x: look_up.get(x, 100)))


if __name__ == "__main__":
    order = "cba"
    s = "abcd"
    print(customSortString(order, s))

"""
First Unique Character in a String

Link: https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

```
s = "leetcode"
return 0.
````

```
s = "loveleetcode"
return 2.
```
"""


def firstUniqChar(s):
    """Index of First Non-Repeating Character

    :type s: str
    :rtype: int
    """

    for idx, i in enumerate(s):
        if s.count(i) == 1:
            return idx
    return -1


s = "loveleetcode"
firstUniqChar(s)

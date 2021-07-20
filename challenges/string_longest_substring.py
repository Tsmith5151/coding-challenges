"""
Longest Substring Without Repeating Characters

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

 
```
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

```
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

```
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

```
Example 4:

Input: s = ""
Output: 0
```
"""


def lengthOfLongestSubstring(s):
    """Determine length of longest substring

    :type s: str
    :rtype: int
    """

    cur_len = 0
    cur_idx = 0
    longest = 0
    dict_ = {}

    for idx, letter in enumerate(s):

        # check if seen and in our current substring
        if letter in dict_ and dict_[letter] >= cur_idx:

            # set start of new substring after duplicate
            cur_idx = dict_[letter] + 1

            # update position
            cur_len = idx - dict_[letter]

            # update position of duplicate
            dict_[letter] = idx

        # not seen letters
        else:
            dict_[letter] = idx
            cur_len += 1
            longest = cur_len if cur_len > longest else cur_len

    return longest


s = "pwwkew"
lengthOfLongestSubstring(s)

""" 
Longest Word in Dictionary

Reference: https://leetcode.com/problems/longest-word-in-dictionary/

Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Example:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
"""


def longestWord(words):
    """
    :type words: List[str]
    :rtype: str
    """
    words = {w: len(w) for w in words}
    return max(words, key=words.get)


if __name__ == "__main__":
    words = ["w", "wo", "wor", "worl", "world"]
    print(longestWord(words))

""" 
Maximum Length of a Concatenated String with Unique Characters

Reference:
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/


You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
Example 4:

Input: arr = ["aa","bb"]
Output: 0
Explanation: Both strings in arr do not have unique characters, thus there are
no valid concatenations.

Solution: if we did a brute force solution, we would have to check every
possible combination of strings. This time complexity would be O(n^2). We will
use backtracking as the solution.
Time Complexity: O(n^2)

Reference: https://www.youtube.com/watch?v=d4SPuvkaeoo
"""

from collections import Counter


def maxLength(arr):
    """
    :type arr: List[str]
    :rtype: int
    """
    chars = set()

    def duplicates(chars, s):
        """
        Helper function to count the number of characters before we add the
        string "s". We are checking the count of each character in the string
        is < 1, meaning there are no duplicates.
        """
        c = Counter(chars) + Counter(s)
        return max(c.values()) > 1

    def backtracking(index):
        # base case: end of the array reached, how long is the
        # concatenated string
        if index == len(arr):
            return len(chars)

        results = 0

        # include the current string if not duplicates in characters
        if not duplicates(chars, arr[index]):
            for c in arr[index]:
                chars.add(c)
            results = backtracking(index + 1)  # continue backtracking

            # clean up the characters set
            for c in arr[index]:
                chars.remove(c)

        # exclude the current string if duplicates in characters
        return max(results, backtracking(index + 1))

    return backtracking(0)


if __name__ == "__main__":
    arr = ["cha", "r", "act", "ers"]
    print(maxLength(arr))

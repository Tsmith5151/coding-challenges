""" 
Partition Labels

Reference: https://leetcode.com/problems/partition-labels/

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Return a list of integers representing the size of these parts.

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]

Solution: for each character in the string, find the last index of that
character in the string.

Time Complexity: O(n)
Memory Complexity: O(26)
"""


def partitionLabels(s):
    """
    :type s: str
    :rtype: List[int]
    """
    # maintain dictionary of last index of each character
    _dict = {k: idx for idx, k in enumerate(s)}
    results = []

    # loop through string
    size = 0
    end_idx = 0
    for i in range(len(s)):

        # identify the last index of current character occurs
        end_idx = max(_dict[s[i]], end_idx)
        size += 1
        if i == end_idx:
            results.append(size)
            size = 0
    return results


if __name__ == "__main__":

    s = "ababcbacadefegdehijhklij"
    print(partitionLabels(s))

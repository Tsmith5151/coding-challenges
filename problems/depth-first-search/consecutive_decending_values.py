"""
Splitting a String Into Descending Consecutive Values

Reference:
https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

You are given a string s that consists of only digits.

Check if we can split s into two or more non-empty substrings such that the
numerical values of the substrings are in descending order and the difference
between numerical values of every two adjacent substrings is equal to 1. 

Example: 
Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.

Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.

Solution: Backtracking (brute force approach)
We check each possible path in the tree and see if any of the paths work out
where the difference between adjacent values is 1. So in some cases we wouldn't
continue on the DFS path, and thus by default are pruning the tree.
"""


def splitString(s):
    """
    :type s: str
    :rtype: bool
    """

    def dfs(index, previous):
        # base case -> end of string
        if index == len(s):
            return True
        for j in range(index, len(s)):  # iterate thru rest of the string
            val = int(s[index : j + 1])
            # note "val" has to be 1 less than the previous value
            # if this is true, then we can call our dfs function
            if val + 1 == previous and dfs(j + 1, val):
                return True

    # determine the first integer
    for i in range(len(s) - 1):  # we need at least 2 separate numbers hence -1
        val = int(s[: i + 1])
        if dfs(i + 1, val):
            return True
    return False


if __name__ == "__main__":
    s = "050043"
    print(splitString(s))

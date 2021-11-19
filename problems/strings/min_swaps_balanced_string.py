"""
Minimum Number of Swaps to Make the String Balanced

Reference:
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
 
You are given a 0-indexed string s of even length n. The string consists of
exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".

Solution: perform swap 
Time Complexity: O(n)
Memory = O(1)
"""


def minSwaps(s):
    """
    :type s: str
    :rtype: int
    """
    if s == "":
        return 0
    # scan thru the string - and keep track of number of extra cosing brackets
    extra_close = 0
    max_extra_close = 0
    for idx, char in enumerate(s):
        # closing bracket
        if char == "]":
            extra_close += 1
        # opening bracket
        else:
            extra_close -= 1
        max_extra_close = max(extra_close, max_extra_close)

    # add + 1 and then divide by 2
    # we will need 1 swap to get rid of the two extra closing brackets
    return (max_extra_close + 1) // 2


if __name__ == "__main__":
    s = "][]["
    print(minSwaps(s))

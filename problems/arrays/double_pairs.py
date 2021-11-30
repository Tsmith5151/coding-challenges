"""
Array of double pairs 

Reference: https://leetcode.com/problems/array-of-doubled-pairs/

Given an integer array of even length arr, return true if it is possible to
reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i <
len(arr) / 2, or false otherwise.

Input: arr = [3,1,3,6]
Output: false

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4]
"""
import collections


def canReorderDoubled(arr):
    """
    :type arr: List[int]
    :rtype: bool

    Greedy search: nlogn
    """
    neg = [i for i in arr if i < 0]
    pos = [i for i in arr if i > 0]
    arr = sorted(neg, reverse=True) + sorted(pos)
    c = collections.Counter(arr)
    for i in arr:
        if c[i] == 0:
            continue
        if c[i * 2] == 0:
            return False
        c[i] -= 1
        c[i * 2] -= 1
    return True


if __name__ == "__main__":
    arr = [4, -2, 2, -4]
    print(canReorderDoubled(arr))

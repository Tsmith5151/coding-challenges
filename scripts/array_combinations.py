""" 
Combinations

Reference: https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Note: we don't want duplicates in the solution.

Solution: Brute Force (backtracking)
Time Complexity: O(n^k); where k = height of tree 
"""


def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    results = []

    def backtrack(start, comb):
        # base case
        if len(comb) == k:
            results.append(comb.copy())
            return
        for i in range(start, n + 1):
            comb.append(i)  # current combination
            backtrack(i + 1, comb)  # recursively call backtrack
            comb.pop()
        return

    backtrack(start=1, comb=[])
    return results


if __name__ == "__main__":
    n = 4
    k = 2
    print(combine(n, k))

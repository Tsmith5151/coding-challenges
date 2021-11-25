""" 
Combination Sum

Reference: https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two
combinations are unique if the frequency of at least one of the chosen numbers
is different.

It is guaranteed that the number of unique combinations that sum up to target is
less than 150 combinations for the given input.

Example:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Solution: Depth First Search
Reference: https://www.youtube.com/watch?v=GBKI9VSKdGg
"""


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    results = []

    def dfs(idx, cur, total):
        # base case: if solution is found
        if total == target:
            # append combination to results
            results.append(cur.copy())
            return
        # if solution is not found (out of bounds or target > total)
        if idx >= len(candidates) or total > target:
            return

        # recursive case:
        cur.append(candidates[idx])

        # left branch: decide to include current candidate
        dfs(idx, cur, total + candidates[idx])

        # right brach: decide to not include current candidate
        # remove element from cur to avoid duplicates
        cur.pop()
        dfs(idx + 1, cur, total)

    # call dfs function
    dfs(idx=0, cur=[], total=0)
    return results


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(combinationSum(candidates, target))

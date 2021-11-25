"""
Combination Sum II
	
Reference: https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate
numbers sum to target. 

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Solution:
Time Complexity: O(2^n)
Reference: https://www.youtube.com/watch?v=rSA3t6BDDwg
"""


def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()  # sort the candidates to avoid duplicates
    results = []

    def backtracking(cur_combination, index, cur_target):
        # Note: everytime we add a candidate, we need to decrease the target we are
        # trying to add up to.

        # base case
        if cur_target == 0:
            results.append(cur_combination.copy())

        if cur_target <= 0:
            return

        # Recursive case
        prev = -1
        for j in range(index, len(candidates)):

            # If we don't want to use the same number twice, we need to skip
            if candidates[j] == prev:
                continue

            cur_combination.append(
                candidates[j]
            )  # append value to the current combination
            backtracking(cur_combination, j + 1, cur_target - candidates[j])
            cur_combination.pop()  # remove the last value from the current combination

            prev = candidates[j]

    backtracking([], 0, target)
    return results


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(combinationSum2(candidates, target))

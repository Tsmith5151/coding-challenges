""" 
Letter Combinations of a Phone Number

Reference: https://leetcode.com/problems/letter-combinations-of-a-phone-number/


Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order. Note that 1 does not map to any letters.

Example:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = "2"
Output: ["a","b","c"]

Solution: dfs
Time complexity: O(n*4^n)
4^n is the number of possible combinations
"""


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    results = []
    if digits == "":
        return None

    mappings = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtracking(i, current):
        """backtracking recursive method"""
        # base case
        if len(current) == len(digits):
            results.append(current)
            return
        # continue building the current combination
        for c in mappings[digits[i]]:
            backtracking(i + 1, current + c)

    backtracking(0, "")
    return results


if __name__ == "__main__":
    digits = "23"
    print(letterCombinations(digits))

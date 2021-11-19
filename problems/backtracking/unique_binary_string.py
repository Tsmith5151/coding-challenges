""" 
Find Unique Binary Sting

Reference: https://leetcode.com/problems/find-unique-binary-string/

Given an array of strings nums containing n unique binary strings each of length
n, return a binary string of length n that does not appear in nums. If there are
multiple answers, you may return any of them.

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Reference: https://www.youtube.com/watch?v=aHqn4Dynd1k

Solution: Backtracking
    root
	/  \
   0     1
  / \   / \
 0  1  1   0
 
Time Complexity = n^2  
"""


def findDifferentBinaryString(nums):
    """
    :type nums: List[str]
    :rtype: str
    """
    unique_strings = {num for num in nums}

    def backtracking(idx, cur_string):
        """
        :type idx: int
        :type cur_string: str
        """
        # base case
        if idx == len(nums):
            res = "".join(cur_string)
            return None if res in unique_strings else res

        # recursive case
        res = backtracking(idx + 1, cur_string)
        if res:
            return res

        # recursive case -> replace with "1"
        cur_string[idx] = "1"
        res = backtracking(idx + 1, cur_string)
        if res:
            return res

    # recursive case -> initialize cur_string with '0'
    return backtracking(0, ["0" for s in nums])


if __name__ == "__main__":
    nums = ["01", "10"]
    print(findDifferentBinaryString(nums))

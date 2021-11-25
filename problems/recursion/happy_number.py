"""
Happy Number

Reference: https://leetcode.com/problems/happy-number/
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Input: n = 19
Output: true

Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 02 = 1

Solution: recursion
Time: O(n)
"""


def isHappy(n: int) -> bool:
    """
    :type n: int
    :rtype: bool
    """
    results = set()

    def sum_of_squares(n):
        """Helper function to compute sum of squares loop"""

        # compute total sum of squares
        n = str(n)
        total = sum([int(n[i]) ** 2 for i in range(len(n))])

        # base case
        if total == 1:
            return True

        # infinite loop
        if total in results:
            return False

        # keep track of results
        results.add(total)
        return sum_of_squares(total)

    return sum_of_squares(n)


if __name__ == "__main__":
    num = 19
    print(isHappy(num))

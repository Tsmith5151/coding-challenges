""" 
Excel Sheet Column Number

Reference: https://leetcode.com/problems/excel-sheet-column-number/

Given a string columnTitle that represents the column title as appear in an
Excel sheet, return its corresponding column number.

Example:
A -> 1
B -> 2
C -> 3

Z -> 26
AA -> 27
AB -> 28 
"""

from string import ascii_uppercase


def titleToNumber(columnTitle):
    """
    :type columnTitle: str
    :rtype: int
    """
    multiplier = 1
    columns = 0
    for s in columnTitle[::-1]:
        columns += (ascii_uppercase.index(s) + 1) * multiplier
        multiplier *= 26
    return columns


if __name__ == "__main__":
    title = "FXSHRXW"
    print(titleToNumber(title))

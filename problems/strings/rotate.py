"""
Rotate String

Link: https://leetcode.com/problems/rotate-string/
    
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
```
Input: A = 'abcde', B = 'cdeab'
Output: true
```

Example 2:
```
Input: A = 'abcde', B = 'abced'
Output: false
```
Note: A and B will have length at most 100.

Note: A queue is a linear structure which follows a particular order in
which the operations are performed. The order is First In First Out (FIFO)
"""


def rotateString(A: str, B: str) -> bool:
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    if A == "" and B == "":
        return True

    a = [i for i in A]
    b = [i for i in B]

    for i in range(len(a)):
        tmp = a[0]
        a.pop(0)
        a.append(tmp)
        if a == b:
            return True
    return False


if __name__ == "__main__":
    A = "abcde"
    B = "cdeab"
    print(rotateString(A, B))

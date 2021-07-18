"""
## Rotations
A left rotation operation on an array shifts each of the array's elements 1
unit to the left. For example, if 2 left rotations are performed on array
[1,2,3,4,5], then the array would become [3,4,5,1,2]. Note that the lowest
index item moves to the highest index in a rotation. This is called a circular
array.
"""


def rotate(l, n):
    return l[n:] + l[:n]


rotate([1, 2, 3, 4, 5], 2)

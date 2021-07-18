from typing import List

"""
Given a sorted array and number N, write a program to find the pairs of numbers
whose sum is equal to N. 
"""


def pair_sum_array(x: List[int], n: int):
    l = [(x[i], x[j]) for i in range(0, len(x)) for j in range(i, len(x))]
    return list(filter(lambda x: (sum(x) == n), l))


n = 8
x = [5, 3, 6, 2, 4, 1]
pair_sum_array(x, n)

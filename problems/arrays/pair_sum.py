"""
Given a sorted array and number N, write a program to find the pairs of numbers
whose sum is equal to N. 
"""


def pair_sum_array(x, n):
    """
    :type x: List[int]
    :type n: int
    :rtype: List[int]
    """
    l = [(x[i], x[j]) for i in range(0, len(x)) for j in range(i, len(x))]
    return list(filter(lambda x: (sum(x) == n), l))


if __name__ == "__main__":
    n = 8
    x = [5, 3, 6, 2, 4, 1]
    print(pair_sum_array(x, n))

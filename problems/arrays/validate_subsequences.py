""" 
Validate Subsequences

Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.

A Subsequence of an array is a set of numbers that are either in the array but
that are in the same order as they appear in the array. For instance, the
numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4].
"""


def isValidSubsequence(array, sequence):
    arridx = 0
    seqidx = 0
    while arridx < len(array) and seqidx < len(sequence):
        if array[arridx] == sequence[seqidx]:
            seqidx += 1
        arridx += 1
    return seqidx == len(sequence)


if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array, sequence))

"""
Minimum Rotations
You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

For example, given the array [7, 1, 3, 2, 4, 5, 6], we perform the following
steps:

"""


def minimumSwaps(x):
    min_num_swaps = 0
    i = 0
    while i < len(x):
        # check to see element == index
        if x[i] != i + 1:
            # if not perform swap and increment
            while x[i] != i + 1:
                temp = x[x[i] - 1]
                x[x[i] - 1] = x[i]
                x[i] = temp
                min_num_swaps += 1
        i += 1
    return min_num_swaps


x = [4, 3, 1, 2]
minimumSwaps(x)

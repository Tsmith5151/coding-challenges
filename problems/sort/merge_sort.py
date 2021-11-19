""" Implement Merge Sort 

Notes:
- merge sort is a divide and conquer algorithm
- recursive as the method calls itself
- very efficient for large datasets
"""
from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted lists into a single sorted list
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using merge sort algorithm
        O(n log n)
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    print("left", left)
    print("right", right)
    return merge(left, right)


if __name__ == "__main__":
    arr = [17, 86, 7, 3, 34, 99, 21, 64]
    print(merge_sort(arr))

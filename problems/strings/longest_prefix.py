"""
Link: https://www.educative.io/edpresso/how-to-find-the-longest-common-prefix-in-an-array-of-strings

Find the longest prefix in an array of strings. A prefix is a collection of
characters at the beginning of a string. For instance, “mi” is a prefix of
“mint” and the longest common prefix between “mint”, “mini”, and “mineral” is
“min”.

Solution: Array
Time Complexity = O(nlogn)
"""


def commonPrefix(arr):
    results = []
    arr = sorted(arr)
    for i in range(0, len(arr[0])):
        if (i + 1 > len(arr[-1])) or (arr[0][i] != arr[-1][i]):
            break
        else:
            results.append(arr[0][i])
    return "".join(results)


words = ["mint", "mini", "mineral"]
commonPrefix(words)

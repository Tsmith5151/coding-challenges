""" 
Replace Elements with Greatest Element on Right Side

Reference:
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.


Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are 


Solution: reverse the array and compute the max element on the right side of
each element. 
Time Complexity: O(n)

Example:
We noticed there is duplicate steps to compute the max value, therefore we
start from the end of the array and compute the max element on the right side
and then decrement the pointer by one for each step. 

[17,18,5,4,6,1] -> index = 0 -> max_val = 18
    [18,5,4,6,1] ->  index = 1 -> max_val = 6
        [5,4,6,1] -> index = 2 -> max_val = 6
           [4,6,1] -> index = 3 -> max_val = 6
              [6,1] -> index = 4 -> max_val = 1
                 [1] -> 5 == -1 for last index
"""


def replaceElements(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    results = [0] * len(arr)
    right_pointer = len(arr) - 1
    prev_max_val = -1

    while right_pointer >= 0:
        if right_pointer + 1 == len(arr):
            results[right_pointer] = -1
        else:
            max_val = max(prev_max_val, arr[right_pointer + 1])
            results[right_pointer] = max_val
        right_pointer -= 1
    return results


if __name__ == "__main__":
    arr = [17, 18, 5, 4, 6, 1]
    print(replaceElements(arr))

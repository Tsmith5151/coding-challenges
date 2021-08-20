""" 
Number of Subarrays with Bounded Maximum

Reference: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

Example:
Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1],
[3].

"""


def numSubarrayBoundedMax(nums, left, right):
    """
    :type nums: List[int]
    :type left: int
    :type right: int
    :rtype: int

    Reference: https://www.youtube.com/watch?v=qse5d1oPzxQ&t=274s
    """
    # Keep track of two stacks: (low range, in bounds)
    # and last index pointer that's in bounds
    l_stack = 0
    i_stack = 0
    output = 0
    last_idx = -1

    for idx, n in enumerate(nums):
        if n < left:
            if i_stack > 0:
                output += i_stack + l_stack
                output -= idx - last_idx - 1
            l_stack += 1
        elif left <= n <= right:
            output += i_stack + l_stack + 1
            i_stack += 1
            last_i = idx
        else:
            l_stack = 0
            i_stack = 0
    return output


if __name__ == "__main__":
    nums = [2, 1, 4, 3]
    left = 2
    right = 3
    print(numSubarrayBoundedMax(nums, left, right))

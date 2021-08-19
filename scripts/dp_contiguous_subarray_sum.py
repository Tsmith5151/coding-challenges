"""
Max Contiguous Subarray Sum

Given an array with integers, return the sum of the subarray with the largest sum. A `subarray` is a subset of the original array that is contiguous and maintains the sequence of all elements from the original array.

Example

```
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The maximum sum subarray goes from index 3 to index 6 with a total sum of 6.
```

[Solution Reference](https://www.youtube.com/watch?v=2MmGzdiKR9Y)

Steps:

- Default to say the the best maximum seen so far is the first element.
- Also default to say the the best max ending at the first element is the first element.
- We are inspecting the item at index i and want to answer the question:
    - "What is the Max Contiguous Subarray Sum we can achieve ending at index i?"
        - 1. **maxEndingHere + nums[i]** 
            - Extend the previous subarray best whatever value it was
            - Let the item we are sitting at contribute to this best max we achieved ending at index i - 1.
        - 2. **nums[i]** 
            - start and end at this index
            - Just take the item we are sitting at's value.
- The `max` of these 2 choices will be the best answer to the Max Contiguous Subarray Sum we can achieve for subarrays ending at index i.
        
Example
```
index     0  1   2  3   4  5  6   7  8
Input: [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
Answer   -2, 1, -2, 4,  3, 5, 6,  1, 5   
```
            
Explanation

```
index 0: [ -2 ]                 (index 0 to index 0)
index 1: [ 1 ]                  (index 1 to index 1) [array ended at index 1]
index 2: [ 1, -3 ]              (index 1 to index 2)
index 3: [ 4 ]                  (index 3 to index 3) [array ended at index 3]
index 4: [ 4, -1 ]              (index 3 to index 4)
index 5: [ 4, -1, 2 ]           (index 3 to index 5)
index 6: [ 4, -1, 2, 1 ]        (index 3 to index 6)
index 7: [ 4, -1, 2, 1, -5 ]    (index 3 to index 7)
index 8: [ 4, -1, 2, 1, -5, 4 ] (index 3 to index 8)
```
    
- Notice how we are changing the end bound by 1 everytime.

"""

from typing import List


def maxSubarraySum(nums: List[int]):
    max_so_far, max_ending_here = nums[0], nums[0]
    for i in range(len(nums) - 1):

        # max(start new subarray, continue subarray)
        max_ending_here = max(nums[i], max_ending_here + nums[i])

        # Did we beat the 'maxSoFar' with the 'maxEndingHere'?
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSubarraySum(nums)

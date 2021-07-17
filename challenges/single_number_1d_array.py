from typing import List
from collections import defaultdict

"""
## Single Number

Link: https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for one. Find that single one. Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

```
Input: [2,2,1]
Output: 1
```
"""


def singleNumber(nums: List[int], results=[]):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Create Default Dictionary
    n_dict = defaultdict(list)
    for n in nums:
        n_dict[n].append(n)

    # Identify the non-dups from dicitonary
    non_dup = [v[0] for k, v in n_dict.items() if len(v) == 1][0]
    return non_dup


singleNumber([2, 2, 1])

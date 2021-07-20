"""
Shuffle String

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.


Example

```python
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
```

```python
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
```
"""


def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    # map each letter with int
    encode = {i: str(s[idx]) for idx, i in enumerate(indices)}
    string = "".join([encode[i] for i in range(0, len(indices))])
    return string


restoreString("aiohn", [3, 1, 4, 2, 0])

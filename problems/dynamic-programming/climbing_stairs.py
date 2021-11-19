"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

Example 2:

```Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

Example 3:

```Input: n = 4
Output: 4
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step + 1 step
2. 1 step + 1 steps + 2 steps
3. 2 steps + 1 step + 1 step
4. 1 step + 2 step + 1 step
5. 2 steps + 2 steps
```

Reference: https://www.youtube.com/watch?v=NFJ3m9a1oJQ
"""

from typing import List
from functools import lru_cache


@lru_cache(maxsize=1000)
def climbStairs(n: int) -> int:
    """Top-Down Approach with Recursion"""
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)


climbStairs(n=6)

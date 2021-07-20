"""
Coin Change

Link: https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:
```

```
Input: coins = [2], amount = 3
Output: -1
Example 3:
Explanation: We cannot make change for 3 with only a 2 coin.
```

```
Input: coins = [1], amount = 0
Output: 0
Example 4:
```

```
Input: coins = [1], amount = 1
Output: 1
Example 5:
```

```
Input: coins = [1], amount = 2
Output: 2
```

[Solution Reference](https://www.youtube.com/watch?v=jgiZlGzXMBw&t=828s)

**Bottom up approach using dynamic programming**

To explain, first we create an array that is called `stack` in the code to keep
track of the minimum ways to make change for each element, where each element
in this array of length(amount) is initially set as a placeholder (amount +1 ).
The goal is to visit all indices in the amount array (e.g. [1,2,3,4,....A])
and then look at all of the subproblems before the current index to determine
what is the minimum number of coins we could use. Note, if we are using coins
[1,2,5] to make change for `11`, then for example, we can only use coins [1,2]
at `amount=4`. 

"""

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    """Bottom Up Approach"""
    stack = [amount + 1] * (amount + 1)
    stack[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                # answer to previous subproblem
                # current amount - coin
                tmp = i - coin
                # tmp + 1 --> we are using a coin
                stack[i] = min(stack[tmp] + 1, stack[i])

    return -1 if stack[amount] > amount else stack[-1]


coinChange(coins=[1, 2, 5], amount=11)

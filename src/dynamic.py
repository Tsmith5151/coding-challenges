# dynamic programming

from typing import List
from functools import lru_cache

def coinChange(coins: List[int], amount: int) -> int:
    """ Bottom Up Approach """
    stack = [amount + 1] * (amount + 1)
    stack[0] = 0
    for i in range(1,amount+1):
        for coin in coins:
            if coin <= i:
                # answer to previous subproblem
                # current amount - coin
                tmp = i - coin
                # tmp + 1 --> we are using a coin 
                stack[i] = min(stack[tmp]+1,stack[i])              
   
    return -1 if stack[amount] > amount else stack[-1]

@lru_cache(maxsize=1000)
def climbStairs(n: int) -> int:
    """ Top-Down Approach with Recursion"""
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)

def universityCareerFair(arrival: List[int], duration: 
                         List[int], counter: int = 0, end: int = 0
):
    arr_dur = sorted(list(zip(arrival, duration)))
    for arr, dur in arr_dur:
        if arr >= end:
            end = arr + dur
            counter += 1
    return counter

# dynamic programming

from typing import List
from functools import lru_cache

@lru_cache(maxsize=1000)
def climbStairs(n: int) -> int:
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

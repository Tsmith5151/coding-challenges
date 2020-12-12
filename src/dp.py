# dynamic programming
from typing import List
from functools import lru_cache


class DynamicProgramming:
    """ solutions to dynamic programming problems"""

    @lru_cache(maxsize=1000)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def universityCareerFair(
        self,arrival: List[int], duration: List[int], counter: int = 0, end: int = 0
    ):
        arr_dur = sorted(list(zip(arrival, duration)))
        for arr, dur in arr_dur:
            if arr >= end:
                end = arr + dur
                counter += 1
        return counter

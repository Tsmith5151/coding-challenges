"""
Find the factorial of an integer. Recall, factorial of a number is the product
of all the integers from 1 to that number. For example, the factorial of 5
(denoted as 6!) is 1 * 2 * 3 * 4 * 5 = 120.

https://www.edureka.co/blog/recursion-in-python/
"""
from functools import lru_cache


@lru_cache(maxsize=1000)
def factorial(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return n
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    n = 5
    results = [(factorial(i)) for i in range(1, n + 1)]
    print(
        f"Factorial: {n} ==> "
        + " * ".join([str(i) for i in range(n, 0, -1)])
        + " = "
        + str(results[-1])
    )

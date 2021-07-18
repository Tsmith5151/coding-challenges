""" 
Find product of two numbers using recursion

5 x 3 = 15
which is broken down to: 5 + 5 + 5 
"""


def product(x: int, y: int):
    if y == 0:
        return 0
    return x + product(x, y - 1)


if __name__ == "__main__":
    x, y = 5, 3
    print(product(x, y))

"""
Determine whether a given integer's sum can be factored down into the sum
of all the squared digits equaling to 1. If so, return True, else enter a
continuous loop.

Example:

Input: 
	19 = 1*1 + 9*1 = 89
	89 = 8*1 + 9*9 = 72
	72 = 6*1 + 7*9 = 42
	42 = 4*1 + 2*9 = 26
	26 = 2*1 + 6*9 = 13
	13 = 1*1 + 3*9 = 10
	10 = 1*1 + 0*1 = 1

Output: True
"""


def check(x: int) -> bool:
    """
    Check if conditions is True

    :param x: int
    """
    if x == 1:
        return True
    else:
        number = [int(str(x)[i]) ** 2 for i in range(len(str(x)))]
        return check(sum(number))


if __name__ == "__main__":
    num = 19
    print(check(num))

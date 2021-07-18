""""
Given a string, find the first uppercase character using recursion
"""


def upper_case(x: str, idx: int = 0) -> str:
    if x[idx].isupper():
        return x[idx]
    if idx == len(x):
        return "No upper case found!"
    else:
        return upper_case(x, idx + 1)


if __name__ == "__main__":
    x = "hello World!"
    print(upper_case(x))

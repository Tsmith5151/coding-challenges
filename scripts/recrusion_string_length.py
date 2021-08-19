"""
Given a string - calculate the length of a string

Reference: https://www.youtube.com/watch?v=RRK0gd77Ln0&list=PL5tcWHG-UPH1K7oTJgIbWy6rCMc8-8Lfm&index=3
"""


def string_length(x: str) -> int:
    if x == "":
        return 0
    return 1 + string_length(x[1:])


if __name__ == "__main__":
    x = "Hello World!"
    print(string_length(x))

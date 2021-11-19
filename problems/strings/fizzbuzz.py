"""
FizzBuzz

Link: https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/743/

Write a program that, given a number n, print out all numbers from 1 to n (inclusive) each on their own line. But there's a catch:

- For numbers divisible by 3, instead of n, print Fizz
- For numbers divisible by 5, instead of n, print Buzz
- For numbers divisible by 3 and 5, just print FizzBuzz
- For example, given the input 1, your program should output:
"""


def fizzbuzz(n):
    """FizzBuzz String Example"""
    if ((n % 3) == 0) and ((n % 5) == 0):
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


n = 15
for i in range(1, n + 1):
    print(fizzbuzz(i))

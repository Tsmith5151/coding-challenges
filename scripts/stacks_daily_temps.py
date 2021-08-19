"""
Daily Temperatures

Link: https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures 

```
T = [73, 74, 75, 71, 69, 72, 76, 73]
```

Output should be:

```
[1, 1, 4, 2, 1, 1, 0, 0]
```

Note: The length of temperatures will be in the range [1, 30000]. Each
temperature will be an integer in the range [30, 100].

Note: a stack is a linear data structure which follows a particular order in which
the operations are performed. The order may be LIFO(Last In First Out)

"""


def dailyTemperatures(T):
    """Compute Temperatures using Stacks"""
    delta = [0] * len(T)
    stack = []
    for i in range(0, len(T)):
        while stack and T[i] > T[stack[-1]]:
            idx = stack.pop()
            delta[idx] = i - idx
        stack.append(i)
    return delta


temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temps))

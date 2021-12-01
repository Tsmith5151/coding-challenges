"""
Daily Temperatures

Link: https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures 


T = [73, 74, 75, 71, 69, 72, 76, 73]
Output should be: [1, 1, 4, 2, 1, 1, 0, 0]

Note: The length of temperatures will be in the range [1, 30000]. Each
temperature will be an integer in the range [30, 100].

Note: a stack is a linear data structure which follows a particular order in which
the operations are performed. The order may be LIFO(Last In First Out)

Solution: Monotonic Decreasing Stack
Time complexity: O(n)
"""


def dailyTemperatures(T):
    """Compute Temperatures using Stacks
    :type T: List[int]
    :rtype: List[int]
    """
    results = [0] * len(T)
    stack = []  # pair of (index,temp)

    for idx, temp in enumerate(T):
        # if stack is empty and temp is greater than temp in stack
        while stack and temp > stack[-1][1]:
            pop_idx, pop_temp = stack.pop()
            # compute days between last lower temp and current temp
            results[pop_idx] = idx - pop_idx
        # once stack is empty, push current temp to stack
        stack.append((idx, temp))
    return results


if __name__ == "__main__":
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(temps))

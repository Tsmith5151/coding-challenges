""" 
Fractional Knapsack problem

Reference: https://www.geeksforgeeks.org/fractional-knapsack-problem/

Given weights and values (or profits) of n items, we need to put these items in a knapsack
of capacity W to get the maximum total value in the knapsack.

Example:
inputs:
weights = [2, 3, 5, 7, 1, 4, 1]
profit = [10, 5, 15, 7, 6, 18, 3]
capacity = 15
output: 55.333    

Solution: Greedy Algorithm
Time Complexity: O(nlogn)

Reference https://www.youtube.com/watch?v=oTTzNMHM05I
"""


def knapsack(weights, profits, capacity):
    """
    :type weights: List[int]
    :type profit: List[int]
    :type capacity: List[int]
    :rtype: int
    """
    # sort the items by their profit/weight ratio
    profit_weights = [(p, w, p / w) for p, w in zip(profits, weights)]
    profit_weights.sort(key=lambda x: x[2], reverse=True)

    # greedily fill the knapsack
    remain = capacity
    max_profit = 0
    for idx, (profit, weight, _) in enumerate(profit_weights):
        if (remain - weight) >= 0:
            remain -= weight
            max_profit += profit
        else:
            fraction = remain / weight
            remain -= fraction
            max_profit += fraction * profit
            break
    return max_profit


if __name__ == "__main__":
    weights = [2, 3, 5, 7, 1, 4, 1]
    profit = [10, 5, 15, 7, 6, 18, 3]
    capacity = 15
    print(knapsack(weights, profit, capacity))

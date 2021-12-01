""" 
Task Scheduler

Reference: https://leetcode.com/problems/task-scheduler/

Given a characters array tasks, representing the tasks a CPU needs to do, where
each letter represents a different task. Tasks could be done in any order. Each
task is done in one unit of time. For each unit of time, the CPU could complete
either one task or just be idle. 

However, there is a non-negative integer n that represents the cooldown period
between two same tasks (the same letter in the array), that is that there must
be at least n units of time between any two same tasks. 

Return the least number of units of times that the CPU will take to finish all
the given tasks. 


Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Solution: Max Heap + Queue
Time Complexity: O(n * m) m = idle tasks; n = number of tasks

Example:
AAABBCC
n = 1

Iteration 1:
Max Heap:
m = [-3,-2,-2]
time = 1 -> after task completed 
q = [(-2, 1 + 1)]

Iteration 2:
m = [-2,-2]
time = 2
q = [(-2, 1 + 1), (-1, 2 + 1)]

Now since time == 2; we can pop queue[0] from list
and add back to the max heap with the count.

Reference: https://www.youtube.com/watch?v=s8p8ukTyA2I
"""
import heapq


def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    # Count number of tasks
    counter = {t: 0 for t in set(tasks)}
    for t in tasks:
        counter[t] = -1 + counter.get(t, 0)

    # Create max heap
    max_heap = list(counter.values())
    heapq.heapify(max_heap)

    queue = []
    time = 0
    while max_heap or queue:  # while at least one is not empty
        time += 1

        if max_heap:
            c = 1 + heapq.heappop(
                max_heap
            )  # count of tasks; subtract since our values are negative.

            if c < 0:  # if count is non-zero
                queue.append([c, time + n])  # add to queue

        # if task is done, remove from queue
        if queue and queue[0][1] == time:
            c = queue.pop(0)[0]  # remove from queue
            heapq.heappush(max_heap, c)

    return time


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(leastInterval(tasks, n))

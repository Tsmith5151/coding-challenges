""" 
Job Sequencing with Deadlines

Reference: https://www.geeksforgeeks.org/job-sequencing-problem/

Given an array of jobs where every job has a deadline and associated profit if
the job is finished before the deadline. It is also given that every job takes
a single unit of time, so the minimum possible deadline for any job is 1

The goal is for the job to complete within the deadline such that the profit is
maximized. Assume each job takes 1 unit of time to complete. 

Constraints: job must be completed within the deadline.

Example:
inputs:
n_jobs = 5
deadlines = [2, 2, 1, 3, 3]
profits - [20, 15, 10, 5, 1]

Solution: Greedy Algorithm
Time Complexity: O(n^2)
"""


from typing import Sequence


def jobSequence(arr, n_jobs):
    """
    :type arr: List[int]
    :type n_jobs:int
    :rtype: int
    """

    # sort profit in desending order
    arr.sort(key=lambda x: x[0], reverse=False)

    slot = [False] * n_jobs
    sequence = [0] * len(arr[0])

    # Find a time slot i, such that slot is empty
    # and i < deadline and i is greatest.
    for idx, (job, deadline, _) in enumerate(arr):
        for j in range(min(n_jobs - 1, arr[idx][1] - 1), -1, -1):
            if slot[j] is False:
                slot[j] = True
                sequence[j] = arr[idx][0]
                break
    return sequence


if __name__ == "__main__":
    n_jobs = 3
    arr = [["a", 2, 20], ["b", 2, 15], ["c", 1, 10], ["d", 3, 5], ["e", 3, 1]]
    print(jobSequence(arr, n_jobs))

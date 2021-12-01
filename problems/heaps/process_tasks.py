"""
Process Tasks Using Servers

Reference: https://leetcode.com/problems/process-tasks-using-servers/

You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​
and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server,
and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds. 

Tasks are assigned to the servers using a task queue. Initially, all servers
are free, and the queue is empty. 

At second j, the jth task is inserted into the queue (starting with the 0th
task being inserted at second 0). As long as there are free servers and the
queue is not empty, the task in the front of the queue will be assigned to a
free server with the smallest weight, and in case of a tie, it is assigned to a
free server with the smallest index.  

If there are no free servers and the queue is not empty, we wait until a server
becomes free and immediately assign the next task. If multiple servers become
free at the same time, then multiple tasks from the queue will be assigned in
order of insertion following the weight and index priorities above. 

A server that is assigned task j at second t will be free again at second t + tasks[j].

Build an array ans​​​​ of length m, where ans[j] is the index of the server the
j​​​​​​th task will be assigned to. 

Return the array ans​​​​.

Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using
  server 2 until second 7.

Solution: Min Heap
Time Complexity: O(mlogn); n = size of servers array; m = number of tasks 
Note: time complexity for a Heap of size n is O(logn). We are using a min heap
here since each time we pop from the heap, we will have the minimum time
remaining for the task the finish.  
"""
import heapq


def assignTasks(servers, tasks):
    """
    :type servers: List[int]
    :type tasks: List[int]
    :rtype: List[int]
    """

    # Create results array to store the server index
    results = [0] * len(tasks)

    # available server -> (weight, index)
    available_servers = [(servers[i], i) for i in range(len(servers))]
    heapq.heapify(available_servers)

    # unavailable servers (time until free, weight, index)
    unavailable_servers = []

    time = 0
    for i in range(len(tasks)):
        time = max(time, i)  # t can be > i

        # all servers are unavailable
        if len(available_servers) == 0:

            # we want the time to advance to where the
            # first server becomes available from the heap
            time = unavailable_servers[0][0]

        # Check all the unavailable servers and see if any become available
        while unavailable_servers and time >= unavailable_servers[0][0]:

            # pop the first server from the heap and make it available
            timefree, weight, index = heapq.heappop(unavailable_servers)
            heapq.heappush(available_servers, (weight, index))

        # at least one server is available; now assign task to that server
        weight, index = heapq.heappop(available_servers)
        heapq.heappush(unavailable_servers, (time + tasks[i], weight, index))

        # update results index
        results[i] = index

    return results


if __name__ == "__main__":
    servers = [3, 3, 2]
    tasks = [1, 2, 3, 2, 1, 2]
    print(assignTasks(servers, tasks))

""" 
Course Schedule II

Reference: https://leetcode.com/problems/course-schedule-ii/

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where prerequisites[i] =
[ai, bi] indicates that you must take course bi first if you want to take course
ai. 

For example, the pair [0, 1], indicates that to take course 0 you have to first
take course 1.  Return the ordering of courses you should take to finish all
courses. If there are many valid answers, return any of them. If it is
impossible to finish all courses, return an empty array. 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]] Output: [0,1] Explanation: There
are a total of 2 courses to take. To take course 1 you should have finished
course 0. So the correct course order is [0,1].  

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] Output:
[0,2,1,3] Explanation: There are a total of 4 courses to take. To take course 3
you should have finished both courses 1 and 2. Both courses 1 and 2 should be
taken after you finished course 0.  So one correct course order is [0,1,2,3].
Another correct ordering is [0,2,1,3].  

Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

Solution: Depth First Search
Reference: https://www.youtube.com/watch?v=Akt3glAwyfY
Time Complexity: O(n + number of prerequisites)
"""

from typing import List


def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """

    # build prerequisites dictionary
    preMap = {i: [] for i in range(numCourses)}
    for course, pre in prerequisites:
        preMap[course].append(pre)

    # create visited mapping along with DFS traversal
    visited = set()

    def dfs(course):

        """Depth First Search - recursive approach"""
        # base case -> if course is already visited, return (avoid loop)
        if course in visited:
            return False  # means this course cannot be completed (loop)

        # if course does not have any prerequisites, return True
        if preMap[course] == []:
            return True

        # currently visiting this course and apply DFS on prerequisites
        visited.add(course)
        for pre in preMap[course]:
            # if DFS return false, means this course cannot be completed
            if not dfs(pre):
                return False

        # otherwise remove course from visited as this is a valid course/prerequisite
        visited.remove(course)
        preMap[course] = []
        return True

    # call DFS for each course
    for course in range(numCourses):
        if not dfs(course):
            return False
    return True


if __name__ == "__main__":
    numCourses = 5
    prereq = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
    print(findOrder(numCourses, prereq))

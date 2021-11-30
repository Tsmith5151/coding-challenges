""" 
Detect Squares

Reference: https://leetcode.com/problems/detect-squares/

You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are
allowed and should be treated as different points. 
Given a query point, counts the number of ways to choose three points from the
data structure such that the three points and the query point form an
axis-aligned square with positive area. 
An axis-aligned square is a square whose edges are all the same length and are
either parallel or perpendicular to the x-axis and y-axis. 

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares
with point point = [x, y] as described above

Solution: Using a hashmap to store the points and find diagonal points. 
Time Complexity: O(1) since we are using a hashmap. 
"""


from typing import DefaultDict


class DetectSquares(object):
    def __init__(self):

        # Use a defaultdict to help handle if keys are not found
        self.map = DefaultDict(int)
        self.points = []

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.map[tuple(point)] += 1
        self.points.append(point)

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        results = 0

        # Extract coordinates from point
        px, py = point[0], point[1]

        # Loop through to find all diagonal points (recall we can have
        # duplicate points)
        for x, y in self.points:
            # The width and height distance should be the same
            # Also the area > 0; so all points cannot be stacked on each other
            if (abs(y - py) == abs(x - px)) or (x == px or y == py):
                continue
            # If top left and bottom right points are found:
            results += self.map([(x, py)] * self.map[(px, y)])


obj = DetectSquares()
obj.add([3, 10])
obj.add([11, 2])
obj.add([3, 2])
obj.count([11, 10])
obj.count([14, 8])
obj.add([11, 2])
obj.count([11, 10])

""" 
Maximum Depth of N-ary Tree

Reference: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal,
each group of children is separated by the null value (See examples).

Example:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Solution: Breadth First Search
Time Complexity: O(n)
"""

import collections


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def maxDepth(root):
    """
    :type root: Node
    :rtype: int
    """

    def bfs(node):
        """Breadth First Search Helper Function"""
        if not node:
            return 0

        depth = 0
        queue = collections.deque()
        queue.append(node)
        while queue:
            # iterate over nodes at current level
            depth += 1
            for j in range(len(queue)):
                node = queue.popleft()
                if node.children:
                    for child in node.children:
                        queue.appendleft(child)
        return depth

    return bfs(root)


if __name__ == "__main__":
    n6 = Node(6)
    n5 = Node(5)
    n4 = Node(3, [n5, n6])
    n3 = Node(2)
    n2 = Node(4)
    n1 = Node(1, [n4, n3, n2])
    print(maxDepth(n1))

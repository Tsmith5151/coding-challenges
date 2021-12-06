""" 
Binary Tree Level Order Traversal
 
Reference:  https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Tree:
                     3
                   /   \
                  9    20 
                       / \
                      15  7

Solution: Breath first search
Time Complexity: O(n)
Memory Complexity: O(n)

Reference: https://www.youtube.com/watch?v=6ZnyEApgFYg
"""


import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    results = []

    def bfs(node):
        """Breath First Search Helper Function"""
        if not node:
            return
        queue = collections.deque()
        queue.append(node)
        while queue:
            level = []  # keep track of the current level
            # iterate over the current level
            for i in range(len(queue)):
                node = queue.popleft()
                if node:  # if node has children
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:  # if level is not empty
                results.append(level)

    bfs(root)
    return results


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    print(levelOrder(tree))

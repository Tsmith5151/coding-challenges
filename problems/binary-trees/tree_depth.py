"""
Maximum Depth of Binary Tree

Leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example:
# 	     3 
# 	   /   \
#     9    20 
#          / \
# 	  	15  7

Input: root = [3,9,20,null,null,15,7]
Output = 3

Solution: Binary Tree
Time Complexity: O(n); in the worst case when the tree becomes unbalanced.
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree(object):
    def __init__(self, val):
        self.root = Node(val)

    def _depth(self, cur_node):
        if cur_node is None:
            return 0
        return 1 + max(self._depth(cur_node.left), self._depth(cur_node.right))

    def max_depth(self):
        if not self.root:
            return 0
        return self._depth(self.root)


if __name__ == "__main__":
    tree = BinaryTree(3)
    tree.root.left = Node(9)
    tree.root.right = Node(20)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(7)

    print(tree.max_depth())

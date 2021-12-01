""" 
Diameter of Binary Tree

Reference: https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root. 

The length of a path between two nodes is represented by the number of edges
between them.

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# 	 1
# 	/ \ 
#    2   3
#   /\
#  4  3

Solution: Binary Tree; bottom-up traversal; this allows us to visit each node
only once. We will also keep track of the height of the tree. We are finding
the diameter of the bottom nodes and working up the top of the tree. For a node
where either the right or left subtree is null, we will replace with -1. 

Time Complexity: O(n)
If we do a top-down traversal, the time complexity is O(n^2).
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        return root

    dfs(root)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(diameterOfBinaryTree(root))

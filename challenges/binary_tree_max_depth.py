"""
Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/

	  3 
	/   \
   9     20 
         / \
	  	15  7

Input: root = [3,9,20,null,null,15,7]
Output = 3
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def inorder(tmp):
    if not tmp:
        return
    inorder(tmp.left)
    print(tmp.val, end=" ")
    inorder(tmp.right)


def maxDepth(root) -> int:
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print("Max Depth:", maxDepth(root))

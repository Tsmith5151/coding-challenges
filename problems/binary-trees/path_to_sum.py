""" 
Path to sum

Reference: https://leetcode.com/problems/path-sum/

Given the root of a binary tree and an integer `targetSum`, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example: 

#           5
#         /   \
#        4     8
#       /      / \
#      11    13   4
#     /  \          \
#    7    2          1
    
path: 5 -> 4 -> 11 -> 2 = 22; Return True 
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    """
    :type root: TreeNode
    :type targetSum: int
    :rtype: bool
    """
    if not root:
        return False

    def dfs(node, curSum):
        """Depth First Search Recursive Helper Function"""
        if not node:
            return False

        # Keep track of current sum
        curSum += node.val

        # if reached leaf node, check if current sum == target
        if node.left is None and node.right is None:
            return curSum == targetSum

        return dfs(node.left, curSum) or dfs(node.right, curSum)

    return dfs(root, 0)


if __name__ == "__main__":

    # Root
    root = TreeNode(5)
    # Right side
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    # Left Side
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    # Target sum
    k = 21
    print(hasPathSum(root, k))

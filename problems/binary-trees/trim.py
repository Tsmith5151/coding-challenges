""" 
Trim a Binary Search Tree

Reference: https://leetcode.com/problems/trim-a-binary-search-tree/

Given the root of a binary search tree and the lowest and highest boundaries as
low and high, trim the tree so that all its elements lies in [low, high].
Trimming the tree should not change the relative structure of the elements that
will remain in the tree (i.e., any node's descendant should remain a
descendant). It can be proven that there is a unique answer. 

Return the root of the trimmed binary search tree. Note that the root may
change depending on the given bounds.

Example:
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Solution: Recursion DFS
Time Complexity: O(n)
Memory Complexity: O(h) -> where h = height of tree
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def trimBST(root, low, high):
    """
    :type root: TreeNode
    :type low: int
    :type high: int
    :rtype: TreeNode
    """

    # if root is null
    if not root:
        return None

    # if root larger than high; trim left subtree
    if root.val > high:
        return trimBST(root.left, low, high)

    # if root less than low; trim right subtree
    if root.val < low:
        return trimBST(root.right, low, high)

    # if root is between boundaries: don't delete the root; update the left and right subtree
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)

    return root


if __name__ == "__main__":
    low, high = 1, 2
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    print(trimBST(root, low, high))

"""
## Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Link: https://leetcode.com/problems/search-in-a-binary-search-tree/


```
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
```

"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if not root:
        return
    if root.val == val:
        return root
    if root.val < val: 
        return searchBST(root.right,val)
    else:
        return searchBST(root.left,val)
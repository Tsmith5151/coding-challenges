""" 
Find Bottom Left Tree Value

Reference: https://leetcode.com/problems/find-bottom-left-tree-value/

Given the root of a binary tree, return the leftmost value in the last row of
the tree.

Example: 
#    2
#   / \
#  1   3

Input: root = [2,1,3]
Output: 1

Example 2:

# 		1 
# 	   / \
#     2   3		
# 	/	 / \ 
#  4	5   6
#  	   /
#     7 

Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree(object):
    def __init__(self, val):
        self.root = Node(val)

    def findBottomLeftValue(self):
        """
        :type root: TreeNode
        :rtype: int
        """
        if self.root.val is None:
            return None
        stack = [self.root]
        left_data = []
        while stack:
            node = stack.pop()
            if node.left:
                left_data.append(node.left.val)
        return left_data[-1]


if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.left = Node(4)
    tree.root.right = Node(3)
    tree.root.left = Node(5)
    tree.root.left = Node(7)
    tree.root.right = Node(6)
    print(tree.findBottomLeftValue())

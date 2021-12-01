"""
Binary Search Tree Validation

Reference: https://www.leetcode.com/problems/validate-binary-search-tree/

1.) Every node of the right subtree has to be larger than current node
2.) Every node on the left subtree is small than the current node
3.) All nodes on the left side of the tree must be less than root node

Solution: We know that the inorder traversal of a binary search tree gives a
sorted order of its elements -- so we will keep track of an array with each
nodes value and the check if final array is in ascending order. 

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
Input: 
			 8 
		    / \
		   3    10
		  / \	/ \
		 1	6  9  11

In order traversal = 1-3-6-8-9-10-11
So this would be a valid tree

Input:

			 5
			/ \
		   1   4
			  / \
			 3	 6

Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def _traversal(self, cur_node):
        """inorder traversal"""
        if cur_node:
            self._traversal(cur_node.left)
            print(cur_node.val)
            self._traversal(cur_node.right)

    def print_traversal(self):
        """print traversal"""
        if self.root:
            self._traversal(self.root)

    def _check(self, cur_node):
        """recursively check each node and append to list"""
        if cur_node is None:
            return
        self._check(cur_node.left)
        self.arr.append(cur_node.val)
        self._check(cur_node.right)

    def is_bst(self):
        """Determine if tree is a Binary Search Tree"""
        self.arr = []
        if self.root:
            self._check(self.root)

        for i in range(0, len(self.arr) - 1):
            if self.arr[i + 1] < self.arr[i]:
                return False
            else:
                return True


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.root = Node(8)
    tree.root.left = Node(3)
    tree.root.right = Node(10)

    print(tree.print_traversal())
    print(tree.is_bst())

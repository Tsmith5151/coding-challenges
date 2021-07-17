"""
Binary Tree: A tree whose elements have at most 2 children is called a binary
tree. Since each element in a binary tree can have only 2 children, we
typically name them the left and right child. 

Reference: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

To insert into a tree we use the same node class created above and add a insert
class to it. The insert class compares the value of the node to the parent node
and decides to add it as a left node or a right node. Finally the PrintTree
class is used to print the tree.

"""

# Reference: https://www.geeksforgeeks.org/binary-tree-set-1-introduction/


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# create root
root = Node(1)
""" following is the tree after above statement
	 1
	/ \
	None None"""

root.left = Node(2)
root.right = Node(3)

"""2 and 3 become left and right children of 1
	   1
	  / \
	 2	 3
	/ \ / \
None None None None"""


root.left.left = Node(4)
"""4 becomes left child of 2
		1
	 /	  \
	2		 3
   / \	    / \
4 None None None
/ \
None None"""

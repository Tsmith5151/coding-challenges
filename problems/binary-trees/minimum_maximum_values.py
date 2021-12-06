"""
Binary Tree: Find the max and min value in a given binary tree

Example: 

# 	     2 
# 	   /   \
#     7     5 
#    /  \    \
#    2   6    9
#    	/ \   /
# 	   5   1  4

Max = 9 - Min = 4
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree(object):
    def __init__(self, val):
        self.root = Node(val)

    def min_max(self):
        """Iterative Solution"""
        if self.root is None:
            return 0
        data = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.left:
                data.append(node.left.val)
                stack.append(node.left)
            if node.right:
                data.append(node.right.val)
                stack.append(node.right)
        return min(data), max(data)


if __name__ == "__main__":
    tree = BinaryTree(3)
    tree.root.left = Node(9)
    tree.root.right = Node(20)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(7)

    _min, _max = tree.min_max()
    print(f"Min Value: {_min} -- Max Value: {_max}")

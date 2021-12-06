"""
Binary Tree: Calculate the size of a binary tree (number of nodes in tree)

#      1
# 	  / \
# 	 2   3
# 	/  \ 
#  4    5

size = 5

Solution: use a stack (last in/ first out) to keep track of all of the nodes visited thus far.
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree(object):
    def __init__(self, val):
        self.root = Node(val)

    def _size(self, cur_node):
        counter = 0

        self.append(cur_node.left)
        self.append(cur_node.right)

        stack = self.stack.pop()
        # check left and right of node and increment counter

    def _size(self, cur_node):
        """
        Recursive Solution
        Break tree down and compute size of the left and
        right subtrees, respectively.
        """
        if cur_node is None:
            return 0
        return 1 + self._size(cur_node.left) + self._size(cur_node.right)

    def size(self):
        """Iterative Solution"""
        if self.root is None:
            return 0
        counter = 1
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.left:
                counter += 1
                stack.append(node.left)
            if node.right:
                counter += 1
                stack.append(node.right)
        return counter


if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right = Node(3)

    print("Iterative", tree.size())
    print("Recursive", tree._size(tree.root))

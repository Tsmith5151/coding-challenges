"""
Pre-order, In-order, and Post-order Traversals:

Reference: https://www.youtube.com/watch?v=6oL-0TdVy28

Example tree:
         _10_
        /     \
       7       11
     /  \        \
    6    8       20
   /      \     /   \
   1      9    14   22
    
- Pre-order:  [10, 7, 6, 1, 8, 9, 11, 20, 14, 22] --> Root -> Left -> Right
- In-order:   [1, 6, 7, 8, 9, 10, 11, 14, 20, 22] --> Left -> Root -> Right
- Post-order: [1, 6, 9, 8, 7, 14, 22, 20, 11, 10]

Example:

preorder: 1-2-4-5-3-6-7
inorder:  4-2-5-1-6-3-7
postorder: 4-2-5-6-3-7-1
levelorder: 1-2-3-4-5-6-7
         1
        /  \
       2     3
     /  \   /  \
    4   5   6   7
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree(Node):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type: str):
        """preorder - postorder - in order"""
        print("Method Type:", traversal_type)
        if traversal_type == "preorder":
            return self.preorder(self.root, "").strip("-")
        elif traversal_type == "inorder":
            return self.inorder(self.root, "").strip("-")
        elif traversal_type == "postorder":
            return self.postorder(self.root, "").strip("-")
        else:
            raise ValueError("Not a valid traversal type!")

    def preorder(self, start, traversal):
        """Root -> Right -> Left"""
        if start:
            traversal += str(start.val) + "-"  # root
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += str(start.val) + "-"  # root
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += str(start.val) + "-"  # root


if __name__ == "__main__":

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right = Node(3)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print(tree.print_tree("preorder"))
    print(tree.print_tree("inorder"))
    # print(tree.print_tree('postorder'))
    print(tree.print_tree("levelorder"))

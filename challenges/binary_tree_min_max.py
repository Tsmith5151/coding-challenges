"""
Find the max and min value in a binary tree

	  2 
	/   \
   7     5 
  /  \    \
  2   6    9
   	 / \   /
	5	1  4

Max = 9
Min = 4
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data


def inorder(tmp):
    if not tmp:
        return
    inorder(tmp.left)
    print(tmp.key, end=" ")
    inorder(tmp.right)


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.left.right.right = Node(1)
    root.right = Node(5)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    inorder(root)

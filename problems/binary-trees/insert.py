""""
Given a binary tree and a key, insert the key into the binary tree at the 
first position available:

Reference:
https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/

Original Tree
# 	   10
# 	  / \
# 	 11	  9
# 	/    / \
#    7    15  8 


Tree after insert 
# 	    10
# 	  /     \
# 	 11	     9
# 	/  \     / \
#    7   12   15  8 


The idea is to do iterative level order traversal of the given tree using queue. If we find a node whose left child is empty, we make new key as left child of the node. Else if we find a node whose right child is empty, we make the new key as right child. We keep traversing the tree until we find a node whose either left or right is empty. 
"""


class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.key, end=" ")
    inorder(temp.right)


def insert(temp, key):
    if not temp:
        root = Node(key)
        return

    # create queue
    q = []
    q.append(temp)

    # order traversal until we find an empty child node to insert
    while len(q):
        temp = q[0]
        q.pop(0)
        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)


if __name__ == "__main__":

    # create tree
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    inorder(root)

    value = 12
    print(f"Insert {value} into Tree")
    insert(root, value)
    inorder(root)

"""
Search if a value exists in a Binary Search Tree

Array: [8,3,10,1,6]
     
	        8
		   / \ 
		  3  10
		 / \
		1   6
"""


class Node:
    def __init__(self, val: int):
        self.right = None
        self.left = None
        self.val = val


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def _insert(self, val, cur_node):
        # add to left
        if val < cur_node.val:
            # add if node does not exist
            if cur_node.left is None:
                cur_node.left = Node(val)
            else:
                self._insert(val, cur_node.left)
        # add to right
        elif val > cur_node.val:
            # add if node does not exist
            if cur_node.right is None:
                cur_node.right = Node(val)
            else:
                self._insert(val, cur_node.right)
        else:
            print("Value already present in tree!")

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _search(self, val: int, cur_node):
        # search left side of tree
        if val < cur_node.val and cur_node.left:
            return self._search(val, cur_node.left)

        # search right side of tree
        elif val > cur_node.val and cur_node.right:
            return self._search(val, cur_node.right)

        if val == cur_node.val:
            return True

    def search(self, val: int):
        if self.root:
            is_found = self._search(val, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(3)
    tree.insert(8)
    tree.insert(1)
    tree.insert(6)

    print(tree.search(3))

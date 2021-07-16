"""
### Pre-order, In-order, and Post-order Traversals:

- Example tree:

```
         _10_
        /     \
       7      11
     /  \      \
    6   8       20
   /    \     /   \
   1    9     14   22
```
    
- Pre-order:  [10, 7, 6, 1, 8, 9, 11, 20, 14, 22]
- In-order:   [1, 6, 7, 8, 9, 10, 11, 14, 20, 22]
- Post-order: [1, 6, 9, 8, 7, 14, 22, 20, 11, 10]



Reference: https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

To insert into a tree we use the same node class created above and add a insert
class to it. The insert class compares the value of the node to the parent node
and decides to add it as a left node or a right node. Finally the PrintTree
class is used to print the tree.

"""
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """Compare the new value with the parent node"""
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
        else:
            self.data = data

            def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
        self.right.PrintTree()

# # Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PrintTree()
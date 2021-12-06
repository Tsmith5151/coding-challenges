""" 
Delete Nodes And Return Forest


Reference: https://leetcode.com/problems/delete-nodes-and-return-forest/
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.


Example 1:

#                      1
#                    /   \
#                   2      3
#                  / \    / \
#                 4   5   6  7 
                 
Output:                 1
 #                   /     \
 #                  2       NA
 #                 / \     /  \
 #                4  NA   6    7 


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]

Solution: Depth First Search
Time Complexity: O(n)
Memory Complexity: O(n + h); where h = height of the tree 

NOTE: A node which does not have any parents is considered as root. So in the
example above, 1,6,7 are considered as roots. 

Check Two Conditions:
root.val is in to_delete or not. 
We need to keep track of the parent of the node as well. 


ToDo: not entirely working as expected. Need to fix it to handle disjoint trees.
"""

import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delNodes(root, to_delete):
    """
    :type root: TreeNode
    :type to_delete: List[int]
    :rtype: List[TreeNode]
    """
    to_delete = set(to_delete)
    results = []

    def dfs(node, delete):
        """Depth First Search Helper Function"""
        # base case
        if not node:
            return

        # root node to be deleted --> get children if any
        if node.val in to_delete:
            if node.left:
                dfs(node.left, True)
            if node.right:
                dfs(node.right, True)
            return False

        # save node value to be deleted
        if delete:
            results.append(node.val)

        # if node is not to be deleted
        else:
            dfs(node.left, False)
            dfs(node.right, False)
            results.append(node.val)

    dfs(root, delete=False)
    return results


if __name__ == "__main__":
    to_delete = [3, 5]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(delNodes(root, to_delete))

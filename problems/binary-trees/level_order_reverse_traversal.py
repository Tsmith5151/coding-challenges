""" 
Binary Tree Level Order Traversal II

Refer to: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Given the root of a binary tree, return the bottom-up level order traversal of
its nodes' values. (i.e., from left to right, level by level from leaf to
root).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

#       3
#     /  \ 
#    9   20             
#        / \
#       15  7      
                          
Solution: Breadth First Search w/ a Queue. We will start from the root node
perform a level order traversal while maintaining two queues. One queue will be
used for iterating over each node at a given level, and another queue (e.g. double-ended queue) for
pushing the visited level to a queue; this way the last level visited will be
the first element in the results array.
Time Complexity: O(n)      
"""

import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    results = collections.deque()

    def bfs(node):
        """Breath First Search Helper Function"""
        queue = collections.deque()
        queue.append(node)
        while queue:
            level = []
            # iterate over each node in the queue
            for j in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                # add node value to the current level list
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # push level array to the results queue
            results.appendleft(level)

    bfs(root)
    return list(results)  # return a list of lists (not a deque)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(levelOrderBottom(root))

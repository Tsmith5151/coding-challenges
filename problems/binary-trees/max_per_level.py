""" 
Find Largest Value in Each Tree Row

Reference: https://leetcode.com/problems/find-largest-value-in-each-tree-row/ 

Given the root of a binary tree, return an array of the largest value in each
row of the tree (0-indexed). 

Example: 
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

                1
              /   \
             3     2 
            / \     \
          5    3     9 


Solution: Breath First Search
Time Complexity: O(n) 
 """

import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largestValues(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    results = []

    def bfs(node):
        """Breath First Search Helper Function"""
        queue = collections.deque()
        queue.append(node)
        while queue:
            max_val = float("-inf")
            # iterate over nodes in current level
            for j in range(len(queue)):
                # pop node from queue
                node = queue.popleft()
                # if child node exists, add to queue
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    # compute max level value
                    max_val = max(max_val, node.val)
            if max_val > 0:
                results.append(max_val)

    bfs(root)
    return results


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)

    print(largestValues(root))

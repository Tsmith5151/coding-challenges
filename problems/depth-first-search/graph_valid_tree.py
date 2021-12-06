""" 
Graph Valid Tree

Reference:  https://www.lintcode.com/problem/178/#
Given a reference of a node in a connected undirected graph.

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge
is a pair of nodes), write a function to check whether these edges make up a
valid tree. 

Example: We want to visit each node and look at the neighbors of each node
recursively, until we've visited to every node connected to this input node.
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Solution: BFS
Time Complexity: O(n)

NOTE: A valid tree is a tree that has no cycles. 
"""


def validTree(n, edges):
    """
    :type n: int
    :type edges: Array
    :rtype: Bool
    """

    # Adjacency list
    adj = {i: [] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    visited = {}

    def dfs(node_i, prev):
        """Depth First Search Helper Function"""
        # if already visited
        if node_i in visited:
            return False
        else:
            visited.add(node_i)
        # iterate over neighbors
        for j in adj[node_i]:
            # if loop is not detected; not really a loop,
            # but backtracking to where we came form
            if j == prev:
                continue
            if not dfs(j, node_i):
                return False
        return True

    # if the number of nodes visited is equal to the number of nodes; connected
    # graph is valid, otherwise not
    return dfs(0, prev=-1) and len(visited) == n


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(validTree(n, edges))

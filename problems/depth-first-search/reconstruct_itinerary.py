""" 
Reconstruct Itinerary

Reference: https://leetcode.com/problems/reconstruct-itinerary/

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
["JFK", "LGB"]. 

Note: smaller lexican order meaning that when sorting the string, you would give ["JFK", "LGA"], which is the smaller lexical order.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example: 
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

Solution: First we need to create an adjacency list. Then we can use DFS to
find the path. Note that we may go along an edge and find out that it is not a
valid path and will have to backtrack and try the other edge.

Time Complexity: O(E) -> E is the number of edges. At worst case, we will have
to backtrack through some edges and therefore could be O(E^2).

Memory Complexity: O(E) -> E is the number of edges. Recursive call stack and
hashmap. 
"""


def adjacency_list(tickets):
    """Helper Function to create Adjacency List
    Adjacency List is a dictionary of from,to key value pairs
    where the values are sorted in lexicographical order.
    """
    _dict = {ticket[0]: [] for ticket in tickets}
    for source, dest in tickets:
        _dict[source] += [dest]
        _dict[source].sort()
    return _dict


def findItinerary(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    results = ["JFK"]

    def dfs(ticket, dest):
        if len(results) == len(tickets) + 1:
            return True

        # invalid path (no outgoing edges): backtrack to source and try other dest
        if dest not in ticket:
            return False

        # valid path: remove dest from ticket
        tmp = ticket[dest]
        for idx, v in enumerate(tmp):
            ticket[dest].pop(idx)
            results.append(v)

            # if end recursive call; return True
            if dfs(ticket, v):
                return True

            # reverse decision (backtrack)
            ticket[dest].insert(idx, v)
            results.pop()
        return False

    ticket = adjacency_list(tickets)
    dfs(ticket, "JFK")
    return results


if __name__ == "__main__":
    tickets = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"],
    ]
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    print(findItinerary(tickets))

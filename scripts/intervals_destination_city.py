"""
Destination City

Link: https://leetcode.com/problems/destination-city/

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example 1
```python
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
```

Example 2
```python
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
```
"""


def destCity(paths):
    """
    :type paths: List[List[str]]
    :rtype: str
    """
    results = [path[1] for path in paths if path[1] not in set([s[0] for s in paths])]
    if results:
        return results[0]
    else:
        return "No Destination!"


paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
destCity(paths)

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


def balancedStringSplit(s):
    """
    :type s: str
    :rtype: int
    """
    counter, total = 0, 0

    for i in s:
        if i == "R":
            counter += 1
        else:
            counter += -1
        if counter == 0:
            total += 1
    
    return total


def reverseString(s):
    """
    :type s: List[str]
    :rtype: List[str]
    """
    return s[::-1]


def firstUniqChar(s):
    """ Index of First Non-Repeating Character
    
    :type s: str
    :rtype: int
    """
    
    for idx,i in enumerate(s):
        if s.count(i) == 1:
            return idx
    return -1
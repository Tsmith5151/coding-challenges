def destCity(paths):
    """
    :type paths: List[List[str]]
    :rtype: str
    """
    results = [
        path[1] for path in paths if path[1] not in set([s[0] for s in paths])
    ]
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

def countNegatives(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    count = 0

    for row in grid:
        if row[-1] >= 0:
            continue
        else:
            count += len(list(filter(lambda x: x < 0, row)))
    return count

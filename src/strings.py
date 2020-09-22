class Strings():
    """ solutions to strings"""
    
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
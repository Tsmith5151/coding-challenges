class Sort():
    """ solutions to strings"""
    def restoreString(s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        encode = {i:str(s[idx]) for idx,i in enumerate(indices)}
        string = ''.join([encode[i] for i in range(0,len(indices))])
        return string
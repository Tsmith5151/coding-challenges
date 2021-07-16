"""
Create grade-school multiplication table 
"""

def multiTable(dim=12):
    """ Create multiplication table up to 12x12"""
    import numpy as np
    table = [[i*idx for i in range(1,dim+1)] for idx in range(1,dim+1)]
    return np.matrix(table)
multiTable()
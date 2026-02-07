import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.asarray(x,dtype = float)
    y = np.asarray(y,dtype = float)
    d = x - y
    return float (np.sum((np.absolute(d))))
    pass
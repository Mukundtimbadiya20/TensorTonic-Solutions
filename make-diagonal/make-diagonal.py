import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    v = np.asarray(v)
    n = len(v)

    m = np.zeros((n,n),dtype = v.dtype)

    for i in range(n):
        m[i,i] = v[i]
    return m
    pass

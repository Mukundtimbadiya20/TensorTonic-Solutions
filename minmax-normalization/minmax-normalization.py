import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    x = np.asarray(X,dtype = float)
    x_min = np.min(x, axis = axis, keepdims = True)
    x_max = np.max(x, axis = axis, keepdims = True)
    denom = x_max - x_min
    x_scaled = (x - x_min)/(np.maximum(denom,eps))
    return x_scaled
    pass
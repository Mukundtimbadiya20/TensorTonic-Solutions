import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    norms = np.linalg.norm(v, axis = -1, keepdims = True) 
    
    norms = np.where(norms == 0, 1.0, norms)
    return v/norms
    pass
    
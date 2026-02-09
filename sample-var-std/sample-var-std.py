import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.asarray(x,dtype = float)
    mean_x = np.mean(x)
    n = x.size
    var = np.sum((x-mean_x)**2) / (n-1)
    std = np.sqrt(var)
    return (var,std)
    pass
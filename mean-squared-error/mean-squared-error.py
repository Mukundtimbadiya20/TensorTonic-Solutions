import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    y_pred = np.asarray(y_pred,dtype = float)
    y_true = np.asarray(y_true,dtype = float)
    
    return float(np.mean((y_pred - y_true) ** 2))
    pass


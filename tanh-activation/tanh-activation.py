import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    exp_pos = np.exp(x)
    exp_neg = np.exp(-x)
    return (exp_pos - exp_neg) / (exp_pos + exp_neg)

    pass
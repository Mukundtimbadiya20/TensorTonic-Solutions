import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    x = np.asarray(x,dtype = float)
    mu0 = float(mu0)
    mean = np.mean(x)
    n = x.size
    s = np.std(x,ddof=1)
    return float((mean - mu0)/(s/np.sqrt(n)))
    pass
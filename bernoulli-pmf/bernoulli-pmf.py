import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    x = np.asarray(x, dtype=int)

    # PMF: p if x==1 else (1-p)
    pmf = np.where(x == 1, p, 1 - p)

    # Moments
    mean = p
    var = p * (1 - p)

    return pmf, float(mean), float(var)

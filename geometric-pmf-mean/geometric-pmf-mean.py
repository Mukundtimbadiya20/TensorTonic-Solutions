import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    k = np.asarray(k, dtype=float)

    # PMF formula (vectorized)
    pmf = (1 - p)**(k - 1) * p

    # Mean of geometric distribution
    mean = 1 / p

    return (pmf, float(mean))

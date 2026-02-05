import numpy as np
import math

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    i = np.arange(0, k + 1)
    pmf = np.exp(-lam) * lam**k / math.factorial(k)
    cdf = np.sum(np.exp(-lam) * lam**i / np.array([math.factorial(j) for j in i]))
    return float(pmf), float(cdf)
    pass
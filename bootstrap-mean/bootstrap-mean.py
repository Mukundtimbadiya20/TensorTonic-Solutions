import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here
  


    x = np.asarray(x, dtype=float)
    N = x.size

    if N == 0:
        raise ValueError("Input array must not be empty")

    # Random generator
    if rng is None:
        rng = np.random.default_rng()

    # Store bootstrap means
    boot_means = np.empty(n_bootstrap)

    # Bootstrap loop
    for b in range(n_bootstrap):
        indices = rng.integers(0, N, size=N)  # sample with replacement
        sample = x[indices]
        boot_means[b] = np.mean(sample)

    # Confidence interval
    alpha = (1 - ci) / 2
    lower = np.quantile(boot_means, alpha)
    upper = np.quantile(boot_means, 1 - alpha)

    return boot_means, float(lower), float(upper)

    pass

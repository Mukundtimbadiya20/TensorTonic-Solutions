import numpy as np
def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.asarray(X, dtype=float)

    # Number of samples
    n = X.shape[0]

    if X.ndim != 2:
        return None

    n_samples, n_features = X.shape

    if n_samples < 2 or n_features < 1:
        return None

        
    # Mean-center the data
    mean = np.mean(X, axis=0)
    X_centered = X - mean

    # Covariance matrix
    cov = (X_centered.T @ X_centered) / (n - 1)

    return cov
    pass 
import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
   


    X = np.asarray(X, dtype=float)
    original_1d = (X.ndim == 1)

    X_imputed = X.copy()

    if original_1d:
        X_imputed = X_imputed.reshape(-1, 1)

    N, D = X_imputed.shape

    for j in range(D):
        col = X_imputed[:, j]

        nan_mask = np.isnan(col)
        valid_mask = np.logical_not(nan_mask)

        if np.any(valid_mask):
            mean_val = np.mean(col[valid_mask])
            col[nan_mask] = mean_val
        else:
            col[:] = 0.0

    # Convert back to 1D if needed
    if original_1d:
        return X_imputed.ravel()

    return X_imputed

    pass
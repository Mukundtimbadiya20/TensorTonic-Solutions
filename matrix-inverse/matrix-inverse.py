import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.asarray(A, dtype=float)

    # Check if square matrix
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None

    try:
        A_inv = np.linalg.inv(A)
        return A_inv
    except np.linalg.LinAlgError:
        # Singular matrix (not invertible)
        return None

import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    m = np.asarray(matrix, dtype=float)

    # Check square matrix
    if m.ndim != 2 or m.shape[0] != m.shape[1]:
        return None

    # Compute eigenvalues
    eigenvalues = np.linalg.eigvals(m)

    # Sort them
    eigenvalues = np.sort(eigenvalues)

    return eigenvalues

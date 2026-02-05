import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.asarray(A)
    n = A.shape[0]
    m = A.shape[1]
    A_t = np.zeros((m,n))

    for i in range(n):
        for j in range(m):
            A_t[j][i] = A[i][j]
    return A_t
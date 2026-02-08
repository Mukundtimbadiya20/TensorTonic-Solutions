import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    diagonal_elements = [A[i][i] for i in range(len(A))]
    # Sum the elements in the new list
    return sum(diagonal_elements)

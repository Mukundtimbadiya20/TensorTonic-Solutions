import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.asarray(C, dtype=float)

    # Row totals
    row_totals = np.sum(C, axis=1)

    # Column totals
    col_totals = np.sum(C, axis=0)

    # Grand total
    total = np.sum(C)

    # Expected frequencies
    expected = np.outer(row_totals, col_totals) / total

    # Chi-square statistic
    chi2 = np.sum((C - expected) ** 2 / expected)

    return float(chi2), expected
    pass
import numpy as np
def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    rater1 = np.asarray(rater1)
    rater2 = np.asarray(rater2)
    n = rater1.size
    p_o = np.sum(rater1 == rater2) / n

    labels = np.unique(np.concatenate([rater1, rater2]))
    p_e = 0.0
    for k in labels:
        p1 = np.sum(rater1 == k) / n
        p2 = np.sum(rater2 == k) / n
        p_e += p1 * p2
    
    denom = 1.0 - p_e
    if denom == 0.0:
        return 1.0 if p_o == 1.0 else 0.0

    return float((p_o - p_e) / denom)
    pass
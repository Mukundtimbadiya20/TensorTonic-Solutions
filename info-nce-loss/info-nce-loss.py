import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    Z1 = np.asarray(Z1, dtype=float)
    Z2 = np.asarray(Z2, dtype=float)

    # Similarity matrix (N x N)
    S = np.dot(Z1, Z2.T) / temperature

    # Numerical stability: subtract row-wise max
    S_stable = S - np.max(S, axis=1, keepdims=True)

    # Softmax denominator
    exp_S = np.exp(S_stable)
    denom = np.sum(exp_S, axis=1)

    # Positive pairs (diagonal elements)
    pos = np.exp(np.diag(S_stable))

    # InfoNCE loss
    loss = -np.mean(np.log(pos / denom))

    return float(loss)
    pass
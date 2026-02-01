import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p (training mode).
    Return (output, dropout_pattern).
    """
    x = np.asarray(x, dtype=float)

    # Choose RNG
    if rng is None:
        random_values = np.random.random(x.shape)
    else:
        random_values = rng.random(x.shape)

    # Create dropout pattern (inverted dropout)
    dropout_pattern = np.where(
        random_values < (1 - p),
        1.0 / (1 - p),
        0.0
    )

    # Apply dropout
    output = x * dropout_pattern

    return output, dropout_pattern

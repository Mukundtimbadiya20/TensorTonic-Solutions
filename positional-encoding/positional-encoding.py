import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """

    # Positions: (seq_len, 1)
    positions = np.arange(seq_len, dtype=float).reshape(-1, 1)

    # Number of sin/cos frequency pairs (ceil(d_model/2))
    num_freqs = (d_model + 1) // 2

    # Frequencies: (1, num_freqs)
    div_term = np.power(
        base,
        (2 * np.arange(num_freqs, dtype=float)) / d_model
    ).reshape(1, -1)

    angles = positions / div_term

    pe = np.zeros((seq_len, d_model), dtype=float)

    # Even indices: sin
    pe[:, 0::2] = np.sin(angles)

    # Odd indices: cos
    pe[:, 1::2] = np.cos(angles[:, : d_model // 2])

    return pe
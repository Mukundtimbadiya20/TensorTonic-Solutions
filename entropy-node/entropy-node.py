import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y) == 0:
        return 0.0
    
    # Get class frequencies
    _, counts = np.unique(y, return_counts=True)
    
    # Calculate probabilities
    probs = counts / len(y)
    
    # Filter out zero probabilities (safety) and compute Shannon entropy
    # Since counts >= 1, probs > 0 is guaranteed by np.unique
    entropy = -np.sum(probs * np.log2(probs))
    
    return float(entropy)
    pass
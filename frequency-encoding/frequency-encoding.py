import numpy as np 
def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    values = np.asarray(values)

    counts={}
    for v in values:
         counts[v] = counts.get(v,0)+1

    n = len(values)

    
    return [counts[v]/n for v in values]
    # Write code here
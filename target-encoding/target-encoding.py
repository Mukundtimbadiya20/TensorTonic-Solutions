import numpy as np
def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    cat = np.asarray(categories)
    t = np.asarray(targets)
    encoded = np.empty(len(cat),dtype = float)

    unique_cats = np.unique(cat)

    for c in unique_cats:
        mean_value = t[cat==c].mean()
        encoded[cat == c] = mean_value
    return encoded.tolist()

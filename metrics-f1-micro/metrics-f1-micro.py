import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    # Invalid input handling
    if y_true.shape != y_pred.shape or y_true.size == 0:
        return None

    # Micro-F1 for single-label multiclass = accuracy
    correct = np.sum(y_true == y_pred)
    total = y_true.size

    return float(correct / total)

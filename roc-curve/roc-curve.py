import numpy as np

def roc_curve(y_true, y_score):
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    # Sort by descending score
    order = np.lexsort((y_true, -y_score))
    y_true = y_true[order]
    y_score = y_score[order]

    # Cumulative TP and FP
    tp = np.cumsum(y_true == 1)
    fp = np.cumsum(y_true == 0)

    # Indices where score changes
    distinct = np.where(np.diff(y_score))[0]
    threshold_idxs = np.r_[distinct, y_true.size - 1]

    tp = tp[threshold_idxs]
    fp = fp[threshold_idxs]
    thresholds = y_score[threshold_idxs]

    # Total positives and negatives
    P = np.sum(y_true == 1)
    N = np.sum(y_true == 0)

    tpr = tp / P if P > 0 else np.zeros_like(tp, dtype=float)
    fpr = fp / N if N > 0 else np.zeros_like(fp, dtype=float)

    # Add starting point only
    tpr = np.r_[0, tpr]
    fpr = np.r_[0, fpr]
    thresholds = np.r_[np.inf, thresholds]

    return fpr, tpr, thresholds

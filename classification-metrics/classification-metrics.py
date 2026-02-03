import numpy as np

import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    # Invalid input
    if y_true.shape != y_pred.shape or y_true.size == 0:
        return None

    n = y_true.size

    # Accuracy (same for all averages)
    accuracy = float(np.mean(y_true == y_pred))

    labels = np.unique(y_true)

    # Helper to compute TP, FP, FN for a class
    def tp_fp_fn(c):
        tp = np.sum((y_true == c) & (y_pred == c))
        fp = np.sum((y_true != c) & (y_pred == c))
        fn = np.sum((y_true == c) & (y_pred != c))
        return tp, fp, fn

    # -------- MICRO --------
    if average == "micro":
        correct = np.sum(y_true == y_pred)
        micro = correct / n
        return {
            "accuracy": micro,
            "precision": micro,
            "recall": micro,
            "f1": micro,
        }

    # -------- BINARY --------
    if average == "binary":
        tp, fp, fn = tp_fp_fn(pos_label)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (2 * precision * recall / (precision + recall)
              if (precision + recall) > 0 else 0.0)
        return {
            "accuracy": accuracy,
            "precision": float(precision),
            "recall": float(recall),
            "f1": float(f1),
        }

    # -------- MACRO / WEIGHTED --------
    precisions, recalls, f1s, supports = [], [], [], []

    for c in labels:
        tp, fp, fn = tp_fp_fn(c)
        support = np.sum(y_true == c)

        p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f = (2 * p * r / (p + r)) if (p + r) > 0 else 0.0

        precisions.append(p)
        recalls.append(r)
        f1s.append(f)
        supports.append(support)

    precisions = np.array(precisions)
    recalls = np.array(recalls)
    f1s = np.array(f1s)
    supports = np.array(supports)

    if average == "macro":
        return {
            "accuracy": accuracy,
            "precision": float(np.mean(precisions)),
            "recall": float(np.mean(recalls)),
            "f1": float(np.mean(f1s)),
        }

    if average == "weighted":
        w = supports / supports.sum()
        return {
            "accuracy": accuracy,
            "precision": float(np.sum(precisions * w)),
            "recall": float(np.sum(recalls * w)),
            "f1": float(np.sum(f1s * w)),
        }

    raise ValueError("Invalid average type")

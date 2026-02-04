import numpy as np

def confusion_matrix_norm(
    y_true,
    y_pred,
    normalize="none",
    num_classes=None,
    eps=1e-12
):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    # ---------- Shape check ----------
    if y_true.shape != y_pred.shape:
        return None

    # ---------- Empty input ----------
    if y_true.size == 0:
        if num_classes is None:
            return None
        K = int(num_classes)
        if normalize == "none":
            return np.zeros((K, K), dtype=int)
        else:
            return np.zeros((K, K), dtype=float)

    # ---------- Determine number of classes ----------
    if num_classes is None:
        K = int(max(y_true.max(), y_pred.max()) + 1)
    else:
        K = int(num_classes)

    # ---------- Validate label range ----------
    if (
        np.any(y_true < 0) or np.any(y_pred < 0) or
        np.any(y_true >= K) or np.any(y_pred >= K)
    ):
        return None

    # ---------- Vectorized bincount ----------
    indices = y_true * K + y_pred
    cm = np.bincount(indices, minlength=K * K).reshape(K, K)

    # ---------- No normalization ----------
    if normalize == "none":
        return cm

    # ---------- Normalize ----------
    cm = cm.astype(float)

    if normalize == "true":
        denom = cm.sum(axis=1, keepdims=True)
        denom[denom == 0] = 1.0
        return cm / (denom + eps)

    if normalize == "pred":
        denom = cm.sum(axis=0, keepdims=True)
        denom[denom == 0] = 1.0
        return cm / (denom + eps)

    if normalize == "all":
        total = cm.sum()
        if total == 0:
            return cm
        return cm / (total + eps)

    raise ValueError("Invalid normalize mode")

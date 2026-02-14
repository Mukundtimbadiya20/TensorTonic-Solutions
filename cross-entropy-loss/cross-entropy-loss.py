import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # Number of samples
    N = y_true.shape[0]

    # Extract probabilities of the correct classes
    correct_class_probs = y_pred[np.arange(N), y_true]

    # Compute mean cross-entropy loss
    loss = -np.mean(np.log(correct_class_probs))

    return loss

    pass
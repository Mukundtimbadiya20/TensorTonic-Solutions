import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    y_train = np.asarray(y_train)
    X_test = np.asarray(X_test)

    # Edge cases
    if y_train.size == 0:
        return np.array([], dtype=int)

    if X_test.size == 0:
        return np.array([], dtype=int)

    # Find majority class
    classes, counts = np.unique(y_train, return_counts=True)
    majority_class = classes[np.argmax(counts)]

    # Predict for all test samples
    predictions = np.full(len(X_test), majority_class, dtype=int)

    return predictions

    pass
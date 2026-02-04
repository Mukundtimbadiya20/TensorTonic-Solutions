def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    num_trees = len(predictions)
    num_samples = len(predictions[0])

    result = []

    # Loop over each sample
    for i in range(num_samples):
        counts = {}

        # Count votes from all trees for sample i
        for t in range(num_trees):
            label = predictions[t][i]
            counts[label] = counts.get(label, 0) + 1

        # Find highest vote count
        max_count = max(counts.values())

        # Among tied classes, pick smallest label
        majority_class = min(
            label for label, cnt in counts.items() if cnt == max_count
        )

        result.append(majority_class)

    return result
def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
        # Top-k items
    top_k = recommended[:k]

    # Convert relevant to set
    relevant_set = set(relevant)

    # Count hits
    hits = sum(1 for item in top_k if item in relevant_set)

    # Compute metrics
    precision = hits / k
    recall = hits / len(relevant_set)

    return [float(precision), float(recall)]
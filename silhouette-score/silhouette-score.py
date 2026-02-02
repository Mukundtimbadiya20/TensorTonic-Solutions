import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here
    x = np.asarray(X)
    labels = np.asarray(labels)
    
    n_samples = x.shape[0]
    unique_labels = np.unique(labels)

    #pairwise distance 
    distance = np.linalg.norm(x[:,None]-x[None,:],axis = 2)
    silhouette_values = np.zeros(n_samples)

    for i in range(n_samples):
        same_cluster = labels == labels[i]

        if np.sum(same_cluster)>1:
            a_i = np.mean(distance[i,same_cluster &(np.arange(n_samples)!=i)])
        else:
            a_i = 0.0
        
        b_i = np.inf
        for c in unique_labels:
            if c != labels[i]:
                cluster_mask = labels == c
                b_i = min(b_i, np.mean(distance[i, cluster_mask]))   
        silhouette_values[i] = (b_i - a_i) / max(a_i, b_i)
    return float(np.mean(silhouette_values))
    pass
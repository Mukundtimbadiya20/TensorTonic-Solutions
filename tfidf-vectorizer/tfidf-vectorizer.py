import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    
    # Handle empty corpus
    if not documents:
        return np.zeros((0, 0)), []

    # Tokenize documents
    tokenized_docs = [doc.lower().split() for doc in documents]

    # Build vocabulary
    vocabulary = sorted(set(
        token
        for doc in tokenized_docs
        for token in doc
    ))

    # Handle corpus with only empty documents
    if not vocabulary:
        return np.zeros((len(documents), 0)), []

    # Word to index mapping
    word_to_idx = {word: idx for idx, word in enumerate(vocabulary)}

    n_docs = len(documents)
    n_vocab = len(vocabulary)

    # Document frequency
    df = Counter()
    for doc in tokenized_docs:
        df.update(set(doc))

    # Initialize TF-IDF matrix
    tfidf_matrix = np.zeros((n_docs, n_vocab))

    # Compute TF-IDF
    for doc_idx, doc in enumerate(tokenized_docs):
        if not doc:
            continue

        tf = Counter(doc)
        doc_len = len(doc)

        for word, count in tf.items():
            tf_value = count / doc_len
            idf_value = math.log(n_docs / df[word])

            col_idx = word_to_idx[word]
            tfidf_matrix[doc_idx, col_idx] = tf_value * idf_value

    return tfidf_matrix, vocabulary
import numpy as np
import math
from collections import Counter

def tfidf_vectorizer(documents):
    
    if not documents:
        return np.array([]), []
    
    # Step 1: Tokenize
    tokenized_docs = [doc.lower().split() for doc in documents]
    
    # Step 2: Vocabulary
    vocab = sorted(set(word for doc in tokenized_docs for word in doc))
    word_to_idx = {word: i for i, word in enumerate(vocab)}
    
    N = len(documents)
    V = len(vocab)
    
    # Step 3: Document Frequency
    df = Counter()
    for doc in tokenized_docs:
        for term in set(doc):
            df[term] += 1
    
    # Step 4: Compute IDF
    idf = {term: math.log(N / df[term]) for term in vocab}
    
    # Step 5: Compute TF-IDF Matrix
    tfidf_matrix = np.zeros((N, V))
    
    for doc_idx, doc in enumerate(tokenized_docs):
        if not doc:
            continue
        
        term_counts = Counter(doc)
        total_terms = len(doc)
        
        for term, count in term_counts.items():
            tf = count / total_terms
            tfidf_matrix[doc_idx, word_to_idx[term]] = tf * idf[term]
    
    return tfidf_matrix, vocab

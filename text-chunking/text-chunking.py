def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    # If tokens are fewer than chunk_size, return one chunk
    if len(tokens) <= chunk_size:
        return [tokens] if tokens else []

    chunks = []
    step = chunk_size - overlap

    for i in range(0, len(tokens) - chunk_size + 1, step):
        chunks.append(tokens[i:i + chunk_size])

    return chunks
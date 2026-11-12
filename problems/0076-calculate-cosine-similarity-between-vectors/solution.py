import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    dots = np.dot(v1,v2)
    sum1 = np.dot(v1,v1)
    sum2 = np.dot(v2,v2)
    return dots / np.sqrt(sum1*sum2)
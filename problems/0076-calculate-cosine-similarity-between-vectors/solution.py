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
    sum1 = 0
    sum2 = 0
    for i in v1:
        sum1 += i*i
    for i in v2:
        sum2 += i*i
    sum1 = np.sqrt(sum1)
    sum2 = np.sqrt(sum2)
    return dots / (sum1*sum2)
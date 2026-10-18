import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    a, b: 1-D vectors of equal length.

    Returns:
        the cosine of the angle between a and b, or 0.0 if either has
        zero length.
    """
    # TODO: Dot product divided by the product of the norms.
    print('type',type(a))
    
    dot=np.dot(a,b)
    norm_a=np.sqrt(np.sum(a**2))
    norm_b=np.sqrt(np.sum(b**2))

    if norm_a ==0 or norm_b ==0:
        return 0.0

    return dot/(norm_a*norm_b)

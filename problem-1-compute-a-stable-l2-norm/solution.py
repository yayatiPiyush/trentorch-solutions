import numpy as np


def solve(x):
    """Implement Compute a Stable L2 Norm from the mathematical contract in README.md."""
    #print(x)
    scale=np.max(np.abs(x))
    x=np.asarray(x)
    return scale*np.sqrt(np.sum((x/scale)**2))

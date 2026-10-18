import numpy as np


def solve(x):
    """Implement Normalize a Vector from the mathematical contract in README.md."""
    print('type',type(x))
    print('shape',np.shape(x))
    print('x is ',x)
    x=np.asarray(x)
    norm=np.sqrt(np.sum(x**2))

    if norm==0:
        raise ValueError()
    return x/norm

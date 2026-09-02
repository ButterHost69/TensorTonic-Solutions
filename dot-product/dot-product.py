import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    sum = 0.0
    for idx in range(len(x)):
        sum += x[idx] * y[idx]
    return sum
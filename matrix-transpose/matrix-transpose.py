import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    shape_y, shape_x = len(A[0]), len(A)
    arr = np.zeros((shape_y, shape_x))
    
    for y_idx, _x in enumerate(A):
        for x_idx, v in enumerate(_x):
            arr[x_idx][y_idx] = v

    return arr
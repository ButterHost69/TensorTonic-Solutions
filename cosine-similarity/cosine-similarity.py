import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a_ = 0
    b_ = 0
    nume = 0.0
    
    for _a, _b in zip(a,b):
        nume += _a *_b
        a_ += _a ** 2
        b_ += _b ** 2

    denom = np.sqrt(a_) * np.sqrt(b_)
    if float(denom) == 0.0 :
        return 0.0 # should be NaN though
    return float(nume / denom)
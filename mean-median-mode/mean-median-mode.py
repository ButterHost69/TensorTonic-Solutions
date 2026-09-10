from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x = sorted(x)
    _len = len(x)
    _sum = 0
    _median = -1
    middle = _len // 2
    if _len % 2:
        _median = x[middle]
    else:
        _median = (x[middle] + x[middle-1]) / 2
    

    counts = {}
    for _x in x:
        _sum += _x
        counts[_x] = counts.get(_x, 0) + 1

    _max, _max_count = 1, -1
    for k,v in counts.items():
        if v > _max_count:
            _max_count = v
            _max = k

    return {
        "mean": _sum / _len,
        "median": float(_median),
        "mode": float(_max),
    }
    
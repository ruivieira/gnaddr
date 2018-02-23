import numpy as np
from typing import List


def levels(data: List[int]) -> np.ndarray:
    """Unique ordered values in data

    Example:
    levels([1,2,2,3,4,5,5,5,5,6])
    >>> array([1,2,3,4,5,6])
    """
    return np.array(sorted(list(set(data))))

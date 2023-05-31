import typing as tp

import numpy as np


def max_element(array: np.ndarray) -> tp.Optional[float]:
    """
    Return max element before zero for input array.
    If appropriate elements are absent, then return None
    :param array: array,
    :return: max element value or None
    """
    if 0 not in array:
        return None
    zero_indices = np.where(array[:-1] == 0)[0]
    if len(zero_indices) == 0:
        return None
    return np.max(array[zero_indices+1])


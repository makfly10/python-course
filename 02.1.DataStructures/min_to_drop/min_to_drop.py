import typing as tp
from collections import Counter

def get_min_to_drop(seq: tp.Sequence[tp.Any]) -> int:
    """
    :param seq: sequence of elements
    :return: number of elements need to drop to leave equal elements
    """
    if seq == [] or len(seq) == 1:
        return 0
    counter_seq = Counter(seq)
    count_drop = 0
    max_value = 0
    for key, value in counter_seq.items():
        if value > max_value:
            max_value = value
    return len(seq) - max_value

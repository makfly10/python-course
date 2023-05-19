import typing as tp


def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    dict_reversed = {}
    for key, value in dct.items():
        if value not in dict_reversed:
            dict_reversed[value] = []
        dict_reversed[value].append(key)
    return dict_reversed
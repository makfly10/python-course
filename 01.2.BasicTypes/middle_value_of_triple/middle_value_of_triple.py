def get_middle_value(a: int, b: int, c: int) -> int:
    """
    Takes three values and returns middle value.
    """
    list_ = []
    list_.append(a)
    list_.append(b)
    list_.append(c)
    list_sort = sorted(list_)
    return list_sort[1]


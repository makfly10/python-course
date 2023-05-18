def reverse_iterative(lst: list[int]) -> list[int]:
    """
    Return reversed list. You can use only iteration
    :param lst: input list
    :return: reversed list
    """
    reversed_lst = []
    lst_index = -1
    while lst_index >= -len(lst):
        reversed_lst.append(lst[lst_index])
        lst_index -= 1
    return reversed_lst

def reverse_inplace_iterative(lst: list[int]) -> None:
    """
    Revert list inplace. You can use only iteration
    :param lst: input list
    :return: None
    """
    if lst == []:
        return lst
    if len(lst) == 1:
        return lst
    low = 0
    high = -1
    while low < (len(lst) //2):
        lst[low], lst[high] = lst[high], lst[low]
        low += 1
        high -= 1

def reverse_inplace(lst: list[int]) -> None:
    """
    Revert list inplace with reverse method
    :param lst: input list
    :return: None
    """
    return lst.reverse()

def reverse_reversed(lst: list[int]) -> list[int]:
    """
    Revert list with `reversed`
    :param lst: input list
    :return: reversed list
    """
    return list(reversed(lst))

def reverse_slice(lst: list[int]) -> list[int]:
    """
    Revert list with slicing
    :param lst: input list
    :return: reversed list
    """
    return lst[::-1]

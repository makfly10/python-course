import typing as tp


def filter_list_by_list_with_set(
        lst_a: tp.Union[list[int], range], lst_b: tp.Union[list[int], range],
) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """
    if lst_a == [] or lst_b == []:
        return lst_a
    if lst_a == lst_b:
        return []

    a_list_goes_before_b = lst_b[0] > lst_a[-1]
    a_list_goes_after_b = lst_a[0] > lst_b[-1]
    if a_list_goes_before_b or a_list_goes_after_b:
        return lst_a
    lst_a_without_b = []
    lists_intersection = set(lst_a).intersection(lst_b)  # O(min(n, m))
    for element in lst_a:  # n
        if element not in lists_intersection:  # O(1)
            lst_a_without_b.append(element)  # O(1)
    return lst_a_without_b


def filter_list_by_list_with_set(
        lst_a: tp.Union[list[int], range], lst_b: tp.Union[list[int], range],
) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """
    pass
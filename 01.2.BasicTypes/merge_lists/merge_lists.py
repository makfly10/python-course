def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    if lst_a == []:
        return lst_b
    if lst_b == []:
        return lst_a
    a_index = 0
    b_index = 0
    lst_ab = []
    while a_index < len(lst_a) and b_index < len(lst_b):
        a_element = lst_a[a_index]
        b_element = lst_b[b_index]
        if a_element > b_element:
            lst_ab.append(b_element)
            b_index += 1
        elif a_element < b_element:
            lst_ab.append(a_element)
            a_index += 1
        else:
            lst_ab.append(a_element)
            lst_ab.append(b_element)
            a_index += 1
            b_index += 1
    if a_index < len(lst_a):
        while a_index < len(lst_a):
            a_element = lst_a[a_index]
            lst_ab.append(a_element)
            a_index += 1
    if b_index < len(lst_b):
        while b_index < len(lst_b):
            b_element = lst_b[b_index]
            lst_ab.append(b_element)
            b_index += 1
    return lst_ab

def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list ising `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    list_a_b = sorted(lst_a + lst_b)
    return list_a_b

import typing as tp


def find_value(nums: tp.Union[list[int], range], value: int) -> bool:
    """
    Find value in sorted sequence
    :param nums: sequence of integers. Could be empty
    :param value: integer to find
    :return: True if value exists, False otherwise
    """
    if nums == [] or value > nums[-1] or value < nums[0]:
        return False
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        if value > nums[middle]:
            low = middle + 1
            high = high + (len(nums) - high)
        elif value < nums[middle]:
            high = middle - 1
        elif value == nums[middle] or value == nums[low] or value == nums[high]:
            return True
    if low > high:
        return False
    return True

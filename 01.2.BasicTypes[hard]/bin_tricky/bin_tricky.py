import typing as tp
import numpy as np


def find_median(nums1: tp.Sequence[int], nums2: tp.Sequence[int]) -> float:
    """
    Find median of two sorted sequences. At least one of sequences should be not empty.
    :param nums1: sorted sequence of integers
    :param nums2: sorted sequence of integers
    :return: middle value if sum of sequences' lengths is odd
             average of two middle values if sum of sequences' lengths is even
    """
    len_nums1_and_nums2 = len(nums1) + len(nums2)
    if nums1 == [] or nums1 == nums2:
        if len(nums2) % 2 != 0:
            return float(nums2[len(nums2) // 2])
        else:
            return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 -1]) / 2
    elif nums2 == []:
        if len(nums1) % 2 != 0:
            return float(nums1[len(nums1) // 2])
        else:
            return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 -1]) / 2
    # elif nums2[0] > nums1[-1] or nums1[0] > nums2[-1]:
    #     if len_nums1_and_nums2 % 2 != 0:
    #         if len(nums1) > len(nums2):
    #             return float(nums1[len_nums1_and_nums2 // 2])
    #         else:
    #             # len(nums1) < len(nums2):
    #             return nums2[(len_nums1_and_nums2 // 2) - len(nums1)]
    #     else:
    #         if len(nums1) > len(nums2):
    #             return (nums1[len_nums1_and_nums2 // 2] + nums1[len_nums1_and_nums2 // 2 - 1]) / 2
    #         elif len(nums1) < len(nums2):
    #             return (nums2[len_nums1_and_nums2 // 2 - len(nums1) - 1] + nums2[len_nums1_and_nums2 // 2 - len(nums1)]) / 2
    #         elif len(nums1) == len(nums2):
    #             if nums2[0] > nums1[-1]:
    #                 return ((nums1[-1] + nums2[0]) / 2)
    #             elif nums1[0] > nums2[-1]:
    #                 return ((nums2[-1] + nums1[0]) / 2)
    # else:
    #     nums_12 = sorted(nums1 + nums2)
    #     return float(np.median(nums_12))

    nums_12 = sorted(nums1 + nums2)
    return float(np.median(nums_12))
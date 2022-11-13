"""EX04 - 'list' Utility Functions."""
__author__ = "730614342"


def all(list0: list[int], n: int) -> bool:
    """Determining whether n is included by list0."""
    if not len(list0):
        return False
    for i in list0:
        if i == n:
            continue
        else:
            return False
    return True


def max(list1: list[int]) -> int:
    """Determining the maximum value in list1."""
    if len(list1) > 0: 
        max_value = list1[0]
        for i in list1:
            if i > max_value:
                max_value = i
        return max_value
    else:
        raise ValueError("max() arg is an empty List")


def is_equal(l1: list[int], l2: list[int]) -> bool:
    """Cheak whether l1 is equal to l2."""
    if not len(l1) == len(l2):
        return False
    for i in range(len(l1)):
        num1 = l1[i]
        num2 = l2[i]
        if num1 == num2:
            continue
        else:
            return False
    return True
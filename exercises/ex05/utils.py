"""EX05 - 'list' Utility Functions."""
__author__ = "730614342"


def only_evens(x: list[int]) -> list:
    """Find the even numbers!"""
    i: int = 0
    list0 = []
    while i < len(x):
        if x[i] % 2 == 0:
            list0.append(x[i])
        i += 1
    return list0


def concat(x: list, y: list) -> list:
    """Generating a new list containing all of the elements!"""
    i: int = 0
    k: int = 0
    list1: list = [] 
    while i < len(x):
        list1.append(x[i])
        i += 1    
    while k < len(y):
        list1.append(y[k])
        k += 1
    return list1


def sub(a_list: list, y: int, z: int) -> list:
    """Generating a list which is a subset of the given list!"""
    list2: list = []
    if y < 0:
        y = 0
    if z > len(a_list):
        z = len(a_list)
    if y == z or y == len(a_list):
        return list2
    while y < z:
        list2.append(a_list[y])
        y += 1
    return list2
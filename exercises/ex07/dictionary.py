
"""EX07 - Dictionary Functions."""
__author__ = "730614342"


from turtle import color


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and the values."""
    output_dict: dict[str, str]
    output_dict = dict()
    for k, v in input_dict.items():
        if v in list(output_dict.keys()):
            raise KeyError()
        output_dict[v] = k 
    return output_dict


def favorite_color(dict1: dict[str, str]) -> str:
    """Finding the color that appears most frequently."""
    values_store: list[str]
    values_store = []
    for v in dict1.values():
        values_store.append(v)
    color_num: dict[str, int]
    color_num = dict()
    for i in values_store:
        if i not in list(color_num.keys()):
            color_num[i] = 1
        else:
            color_num[i] += 1
    values = list(color_num.values())
    keys = list(color_num.keys())
    index1 = values.index(max(values))
    result = keys[index1]
    return result


def count(list1: list[str]) -> dict[str, int]:
    """Counting the number of times that calue appeared in the input list."""
    dict1: dict[str, int]
    dict1 = dict()
    for i in list1:
        if i not in list(dict1.keys()):
            dict1[i] = 1
        else:
            dict1[i] += 1
    return dict1




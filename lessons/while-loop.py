def sub(a_list: list[int], y: int, z: int) -> list:
    """Generating a list which is a subset of the given list!"""
    list2 = list[int] = []
    i: int = 0
    if a_list == [] or y > len(a_list) or z <= 0:
        return [] 
    if y < 0:
        y = 0
    while y < z:
        list2.append(a_list[y])
        y += 1

a_list = [10, 20, 30, 40]
print(sub(a_list, 1, 3))

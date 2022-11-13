"""Unit Tests."""
 
__author__ = "730614342"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Find the even numbers!"""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_many() -> None:
    """Find the even numbers!"""
    x: list[int] = [1, 2, 3, 4]
    assert only_evens(x) == [2, 4]


def test_only_evens_single() -> None:
    """Find the even numbers!"""
    x: list[int] = [2]
    assert only_evens(x) == [2]


def test_concat_emmpty() -> None:
    """Generating a new list containing all of the elements!"""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_many() -> None:
    """Generating a new list containing all of the elements!"""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]


def test_concat_single() -> None:
    """Generating a new list containing all of the elements!"""
    x: list[int] = [1]
    y: list[int] = [2]
    assert concat(x, y) == [1, 2]


def test_sub_empty() -> None:
    """Generating a list which is a subset of the given list!"""
    a_list: list[int] = []
    y: int = 0
    z: int = 0
    assert sub(a_list, y, z) == []


def test_sub_many() -> None:
    """Generating a list which is a subset of the given list!"""
    a_list: list[int] = [10, 20, 30, 40]
    y: int = 1
    z: int = 3
    assert sub(a_list, y, z) == [20, 30]


def test_sub_other() -> None:
    """Generating a list which is a subset of the given list!"""
    a_list: list[int] = [10, 20, 30, 40]
    y: int = 3
    z: int = 3
    assert sub(a_list, y, z) == []
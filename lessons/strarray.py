"""Examples of "vectorized" operations via magic methods."""

from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"


a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
#
b: StrArray = StrArray(["Bacot", "NAnce", "Black"])
print(a)




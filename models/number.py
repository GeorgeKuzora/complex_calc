from typing import Protocol, Self


class Number(Protocol):

    def __add__(self, number: Self) -> Self: ...

    def __sub__(self, number: Self) -> Self: ...

    def __mul__(self, number: Self) -> Self: ...

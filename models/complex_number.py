from typing import Self


class ComplexNumber:
    def __init__(self, real: float, imaginary: float) -> None:
        self._real = real
        self._imaginary = imaginary

    def to_tuple(self) -> tuple[float, float]:
        return (self._real, self._imaginary)

    def __add__(self, number: Self) -> Self:
        real = self._real + number.to_tuple()[0]
        imaginary = self._imaginary + number.to_tuple()[1]
        return ComplexNumber(real, imaginary)

    def __sub__(self, number: Self) -> Self:
        real = self._real - number.to_tuple()[0]
        imaginary = self._imaginary - number.to_tuple()[1]
        return ComplexNumber(real, imaginary)

    def __mul__(self, number: Self) -> Self:
        real = (
            self._real * number.to_tuple()[0] - self._imaginary * number.to_tuple()[1]
        )
        imaginary = (
            self._real * number.to_tuple()[1] + self._imaginary * number.to_tuple()[1]
        )
        return ComplexNumber(real, imaginary)

    def __str__(self):
        if self._imaginary >= 0:
            return f"{self._real}+{self._imaginary}i"
        return f"{self._real}{self._imaginary}i"

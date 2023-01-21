from __future__ import annotations

class rational:

    def __init__(self, /, num: int, den: int=1) -> None:
        self.num = num
        self.den = den

    @staticmethod
    def from_float(number: float, /) -> rational:
        return ...
    
    def to_float(self, /) -> float:
        return self.num / self.den
    
    def __add__(self, value: rational, /) -> rational:
        ...

    def __sub__(self, value: rational, /) -> rational:
        ...

    def __mul__(self, value: rational, /) -> rational:
        ...

    def __truediv__(self, value: rational, /) -> rational:
        ...

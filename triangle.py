from dataclasses import dataclass
from enum import Enum, auto


class TriangleType(Enum):
    EQUILATERAL = auto()
    ISOSCELES = auto()
    SCALENE = auto()
    INVALID = auto()


@dataclass(frozen=True, slots=True)
class Triangle:
    side1: int
    side2: int
    side3: int

    def __post_init__(self) -> None:
        if not all(isinstance(side, int) and not isinstance(side, bool) for side in (self.side1, self.side2, self.side3)):
            raise ValueError("Triangle sides must be integers")

    @property
    def type(self) -> TriangleType:
        a, b, c = self.side1, self.side2, self.side3

        if a <= 0 or b <= 0 or c <= 0:
            return TriangleType.INVALID
        if a == b == c:
            return TriangleType.EQUILATERAL
        if a >= b + c or b >= a + c or c >= a + b:
            return TriangleType.INVALID
        if a == b or a == c or b == c:
            return TriangleType.ISOSCELES
        return TriangleType.SCALENE

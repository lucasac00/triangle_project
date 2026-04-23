from dataclasses import dataclass
from enum import Enum, auto

class TriangleSideType(Enum):
    EQUILATERAL = auto()
    ISOSCELES = auto()
    SCALENE = auto()
    INVALID = auto()

class TriangleAngleType(Enum):
    RIGHT = auto()
    ACUTE = auto()
    OBTUSE = auto()
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
    def side_type(self) -> TriangleSideType:
        a, b, c = sorted((self.side1, self.side2, self.side3))

        if a <= 0 or a + b <= c:
            return TriangleSideType.INVALID
        if a == b == c:
            return TriangleSideType.EQUILATERAL
        if a == b or b == c:
            return TriangleSideType.ISOSCELES
        return TriangleSideType.SCALENE

    @property
    def angle_type(self) -> TriangleAngleType:
        a, b, c = sorted((self.side1, self.side2, self.side3))

        if a <= 0 or a + b <= c:
            return TriangleAngleType.INVALID
        
        sq_sum = a**2 + b**2
        c_sq = c**2

        if c_sq == sq_sum:
            return TriangleAngleType.RIGHT
        if c_sq > sq_sum:
            return TriangleAngleType.OBTUSE
        return TriangleAngleType.ACUTE

    @property
    def type(self) -> TriangleSideType:
        return self.side_type

    @property
    def side_message(self) -> str:
        if self.side_type == TriangleSideType.INVALID:
            return f"📐 This sides {self.side1} {self.side2} {self.side3} is invalid"
        return f"📐 This sides {self.side1} {self.side2} {self.side3} is {self.side_type.name.lower()}"

    @property
    def angle_message(self) -> str:
        if self.angle_type == TriangleAngleType.INVALID:
            return f"📐 This sides {self.side1} {self.side2} {self.side3} is invalid"
        return f"📐 This sides {self.side1} {self.side2} {self.side3} is {self.angle_type.name.lower()} triangle"


def run_cli() -> None:
    side1 = int(input("Enter side 1: "))
    side2 = int(input("Enter side 2: "))
    side3 = int(input("Enter side 3: "))
    triangle = Triangle(side1, side2, side3)
    print(triangle.side_message)
    print(triangle.angle_message)


if __name__ == "__main__":
    run_cli()
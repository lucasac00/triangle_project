import pytest
from triangle import Triangle, TriangleType


def test_equilateral():
    t = Triangle(7, 7, 7)
    assert t.type == TriangleType.EQUILATERAL

def test_scalene():
    t = Triangle(3, 4, 5)
    assert t.type == TriangleType.SCALENE

def test_isoceles():
    t = Triangle(10, 10, 12)
    assert t.type == TriangleType.ISOSCELES

def test_string():
    t1 = "a"
    t2 = "b"
    t3 = 10

    with pytest.raises(ValueError):
        Triangle(t1, t2, t3)

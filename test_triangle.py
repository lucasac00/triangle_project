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

def test_invalid():
    t = Triangle(1, 1, 5)
    assert t.type == TriangleType.INVALID

def test_negative():
    t = Triangle(-1, 2, 3)
    assert t.type == TriangleType.INVALID

def test_all_sides_zero():
    t = Triangle(0, 0, 0)
    assert t.type == TriangleType.INVALID

def test_float_numbers():
    t1 = 0.12
    t2 = 0.004
    t3 = 0.156
    with pytest.raises(ValueError):
        Triangle(t1, t2, t3) 

def test_string():
    t1 = "a"
    t2 = "b"
    t3 = 10

    with pytest.raises(ValueError):
        Triangle(t1, t2, t3)

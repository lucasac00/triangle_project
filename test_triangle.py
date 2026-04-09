import pytest
from triangle import Triangle, TriangleType


def test_equilateral():
    t1 = 7
    t2 = 7
    t3 = 7

    t = Triangle(t1, t2, t3)
    assert t.type == TriangleType.EQUILATERAL

def test_scalene():
    t1 = 3
    t2 = 4
    t3 = 5

    t = Triangle(t1, t2, t3)
    assert t.type == TriangleType.SCALENE

def test_isoceles():
    t1 = 10
    t2 = 10
    t3 = 12

    t = Triangle(t1, t2, t3)
    assert t.type == TriangleType.ISOSCELES

def test_invalid():
    t1 = 1
    t2 = 1
    t3 = 5  

    t = Triangle(t1, t2, t3)
    assert t.type == TriangleType.INVALID

def test_negative():
    t1 = -1
    t2 = 2
    t3 = 3

    t = Triangle(t1, t2, t3)
    assert t.type == TriangleType.INVALID

def test_all_sides_zero():
    t1 = 0
    t2 = 0
    t3 = 0

    t = Triangle(t1, t2, t3)
    assert t.type == TriangleType.INVALID

def test_float_numbers():
    t1 = 0.012
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

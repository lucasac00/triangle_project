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
        
def test_boolean():
    with pytest.raises(ValueError):
        Triangle(True, False, True)
        
def test_sum_equals_third_side():
    t = Triangle(2, 3, 5)
    assert t.type == TriangleType.INVALID

def test_isoceles_diff():
    # side1 == side3 & side2 == side3
    t1 = Triangle(10, 12, 10)
    t2 = Triangle(12, 10, 10)
    assert t1.type == TriangleType.ISOSCELES
    assert t2.type == TriangleType.ISOSCELES

def test_invalid_diff():
    t1 = Triangle(5, 1, 1)
    t2 = Triangle(1, 5, 1)
    assert t1.type == TriangleType.INVALID
    assert t2.type == TriangleType.INVALID
    
def test_single_zero():
    # only one side = 0
    t = Triangle(0, 3, 4)
    assert t.type == TriangleType.INVALID

## Lucas de Araújo Cardoso - 813583
## Arthur Braga da Fonseca - 811461
## Samuel Said - 800209

import pytest
from triangle import Triangle, TriangleSideType, TriangleAngleType, run_cli

def test_equilateral():
    t1 = 7
    t2 = 7
    t3 = 7

    t = Triangle(t1, t2, t3)
    assert t.side_type == TriangleSideType.EQUILATERAL, f"Expected EQUILATERAL for sides {t1}, {t2}, {t3} but got {t.side_type}"
    assert t.reason is None
    print("Test passed: Equilateral triangle with sides 7, 7, 7 correctly identified")

def test_scalene():
    t1 = 3
    t2 = 4
    t3 = 5

    t = Triangle(t1, t2, t3)
    assert t.side_type == TriangleSideType.SCALENE, f"Expected SCALENE for sides {t1}, {t2}, {t3} but got {t.side_type}"
    assert t.reason is None
    print("Test passed: Scalene triangle with sides 3, 4, 5 correctly identified")

def test_isoceles():
    t1 = 10
    t2 = 10
    t3 = 12

    t = Triangle(t1, t2, t3)
    assert t.side_type == TriangleSideType.ISOSCELES, f"Expected ISOSCELES for sides {t1}, {t2}, {t3} but got {t.side_type}"
    assert t.reason is None
    print("Test passed: Isosceles triangle with sides 10, 10, 12 correctly identified")

def test_invalid():
    t1 = 1
    t2 = 1
    t3 = 5  

    t = Triangle(t1, t2, t3)
    assert t.side_type == TriangleSideType.INVALID, f"Expected INVALID for sides {t1}, {t2}, {t3} but got {t.side_type}"
    assert t.reason == "This triangle is invalid because the sum of sides 1 and 1 is not greater than side 5"
    print("Test passed: Invalid triangle with sides 1, 1, 5 correctly identified as invalid")

def test_negative():
    t1 = -1
    t2 = 2
    t3 = 3

    t = Triangle(t1, t2, t3)
    assert t.side_type == TriangleSideType.INVALID, f"Expected INVALID for sides {t1}, {t2}, {t3} but got {t.side_type}"
    assert t.reason == "This triangle is invalid because side(s) -1 are not positive"

def test_all_sides_zero():
    t1 = 0
    t2 = 0
    t3 = 0

    t = Triangle(t1, t2, t3)
    assert t.side_type == TriangleSideType.INVALID, f"Expected INVALID for sides {t1}, {t2}, {t3} but got {t.side_type}"
    assert t.reason == "This triangle is invalid because side(s) 0, 0, 0 are not positive"

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
        
def test_boolean():
    with pytest.raises(ValueError):
        Triangle(True, False, True)
        
def test_sum_equals_third_side():
    t = Triangle(2, 3, 5)
    assert t.side_type == TriangleSideType.INVALID, f"Expected INVALID for sides {t.side1}, {t.side2}, {t.side3} but got {t.side_type}"
    assert t.reason == "This triangle is invalid because the sum of sides 2 and 3 is not greater than side 5"

def test_isoceles_diff():
    # side1 == side3 & side2 == side3
    t1 = Triangle(10, 12, 10)
    t2 = Triangle(12, 10, 10)
    assert t1.side_type == TriangleSideType.ISOSCELES, f"Expected ISOSCELES for sides {t1.side1}, {t1.side2}, {t1.side3} but got {t1.side_type}"
    assert t1.reason is None
    assert t2.side_type == TriangleSideType.ISOSCELES, f"Expected ISOSCELES for sides {t2.side1}, {t2.side2}, {t2.side3} but got {t2.side_type}"
    assert t2.reason is None

def test_invalid_diff():
    t1 = Triangle(5, 1, 1)
    t2 = Triangle(1, 5, 1)
    assert t1.side_type == TriangleSideType.INVALID, f"Expected INVALID for sides {t1.side1}, {t1.side2}, {t1.side3} but got {t1.side_type}"
    assert t1.reason == "This triangle is invalid because the sum of sides 1 and 1 is not greater than side 5"
    assert t2.side_type == TriangleSideType.INVALID, f"Expected INVALID for sides {t2.side1}, {t2.side2}, {t2.side3} but got {t2.side_type}"
    assert t2.reason == "This triangle is invalid because the sum of sides 1 and 1 is not greater than side 5"
    
def test_single_zero():
    # only one side = 0
    t = Triangle(0, 3, 4)
    assert t.side_type == TriangleSideType.INVALID, f"Expected INVALID for sides {t.side1}, {t.side2}, {t.side3} but got {t.side_type}"
    assert t.reason == "This triangle is invalid because side(s) 0 are not positive"


def test_right_angle():
    t = Triangle(3, 4, 5)
    assert t.angle_type == TriangleAngleType.RIGHT, f"Expected RIGHT angle for sides {t.side1}, {t.side2}, {t.side3} but got {t.angle_type}"
    assert t.reason is None
    print("Test passed: Right-angled triangle with sides 3, 4, 5 correctly identified")


def test_acute_angle():
    t = Triangle(4, 5, 6)
    assert t.angle_type == TriangleAngleType.ACUTE, f"Expected ACUTE angle for sides {t.side1}, {t.side2}, {t.side3} but got {t.angle_type}"
    assert t.reason is None


def test_obtuse_angle():
    t = Triangle(2, 3, 4)
    assert t.angle_type == TriangleAngleType.OBTUSE, f"Expected OBTUSE angle for sides {t.side1}, {t.side2}, {t.side3} but got {t.angle_type}"
    assert t.reason is None


def test_invalid_angle():
    t = Triangle(1, 2, 3)
    assert t.angle_type == TriangleAngleType.INVALID, f"Expected INVALID angle for sides {t.side1}, {t.side2}, {t.side3} but got {t.angle_type}"
    assert t.reason == "This triangle is invalid because the sum of sides 1 and 2 is not greater than side 3"

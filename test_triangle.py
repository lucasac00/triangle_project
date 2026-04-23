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
    assert t.side_type == TriangleSideType.EQUILATERAL

def test_scalene():
    t1 = 3
    t2 = 4
    t3 = 5

    t = Triangle(t1, t2, t3)
    assert t.side_type == TriangleSideType.SCALENE

def test_isoceles():
    t1 = 10
    t2 = 10
    t3 = 12

    t = Triangle(t1, t2, t3)
    assert t.side_type == TriangleSideType.ISOSCELES

def test_invalid():
    t1 = 1
    t2 = 1
    t3 = 5  

    t = Triangle(t1, t2, t3)
    assert t.side_type == TriangleSideType.INVALID

def test_negative():
    t1 = -1
    t2 = 2
    t3 = 3

    t = Triangle(t1, t2, t3)
    assert t.side_type == TriangleSideType.INVALID

def test_all_sides_zero():
    t1 = 0
    t2 = 0
    t3 = 0

    t = Triangle(t1, t2, t3)
    assert t.side_type == TriangleSideType.INVALID

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
    assert t.side_type == TriangleSideType.INVALID

def test_isoceles_diff():
    # side1 == side3 & side2 == side3
    t1 = Triangle(10, 12, 10)
    t2 = Triangle(12, 10, 10)
    assert t1.side_type == TriangleSideType.ISOSCELES
    assert t2.side_type == TriangleSideType.ISOSCELES

def test_invalid_diff():
    t1 = Triangle(5, 1, 1)
    t2 = Triangle(1, 5, 1)
    assert t1.side_type == TriangleSideType.INVALID
    assert t2.side_type == TriangleSideType.INVALID
    
def test_single_zero():
    # only one side = 0
    t = Triangle(0, 3, 4)
    assert t.side_type == TriangleSideType.INVALID


def test_right_angle():
    t = Triangle(3, 4, 5)
    assert t.angle_type == TriangleAngleType.RIGHT


def test_acute_angle():
    t = Triangle(4, 5, 6)
    assert t.angle_type == TriangleAngleType.ACUTE


def test_obtuse_angle():
    t = Triangle(2, 3, 4)
    assert t.angle_type == TriangleAngleType.OBTUSE


def test_invalid_angle():
    t = Triangle(1, 2, 3)
    assert t.angle_type == TriangleAngleType.INVALID

def test_cli_input(monkeypatch, capsys):
    inputs = iter(["3", "4", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    run_cli()

    captured = capsys.readouterr()
    assert "this sides 3 4 5 is scalene" in captured.out
    assert "this sides 3 4 5 is right triangle" in captured.out


def test_cli_input_invalid(monkeypatch, capsys):
    inputs = iter(["1", "2", "3"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    run_cli()

    captured = capsys.readouterr()
    assert "this sides 1 2 3 is invalid" in captured.out
    assert captured.out.count("this sides 1 2 3 is invalid") == 2

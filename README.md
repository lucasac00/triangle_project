# Triangle Problem (Python + pytest)

This repository contains a Python implementation of the classic **Triangle Problem**, commonly used in software testing.

## Problem

Given three integers representing the sides of a triangle, the program must classify it as:

- **EQUILATERAL** — all sides equal  
- **ISOSCELES** — two sides equal  
- **SCALENE** — all sides different  
- **INVALID** — does not form a valid triangle  

---

##  Setup

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
pip install pytest
```

## Running Tests

Run all tests:
```bash
python -m pytest
```

Run a specific test with verbose output (shows pass messages):
```bash
python -m pytest -s test_triangle.py::test_equilateral
```

## Usage

Run the interactive CLI:
```bash
python triangle.py
```
from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 1) == 4

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(7, 0) == "Error: cannot divide by zero"
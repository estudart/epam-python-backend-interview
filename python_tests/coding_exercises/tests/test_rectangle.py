import pytest

from src.shapes import Rectangle



def test_area(rectagle: Rectangle, dimensions):
    length, width = dimensions
    assert rectagle.area() == length*width


def test_perimeter(rectagle: Rectangle, dimensions):
    length, width = dimensions
    assert rectagle.perimeter() == 2*length + 2*width


def test_not_equal(rectagle, weird_rectangle):
    assert rectagle != weird_rectangle



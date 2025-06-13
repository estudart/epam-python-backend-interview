import pytest

from src.shapes import Rectangle



@pytest.fixture
def dimensions():
    return 10, 20


@pytest.fixture
def rectagle(dimensions):
    length, width = dimensions
    return Rectangle(length=length, width=width)


@pytest.fixture
def weird_rectangle():
    return Rectangle(length=5, width=6)
import pytest
import math

from src.shapes import Circle, Rectangle


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = Circle(10)


    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle


    def test_radius(self):
        assert self.circle.area() == (
            math.pi * self.circle.radius ** 2
        )

    
    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected
    

    def test_not_same_area_rectangle(self, rectangle: Rectangle):
        assert self.circle.area != rectangle.area
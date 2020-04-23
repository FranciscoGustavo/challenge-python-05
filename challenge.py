import math


def square_area(side):
    """Returns the area of a square"""
    area = side * side
    return round(area, 1)


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    area = base * height
    return round(area, 1)


def triangle_area(base, height):
    """Returns the area of a triangle"""
    area = (base * height) / 2
    return round(area, 1)

def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    area = (diagonal_1 * diagonal_2) / 2
    return round(area, 1)

def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    area = ((base_minor + base_major) / 2) * height
    return round(area, 1)

def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    area = (perimeter * apothem) / 2
    return round(area, 1)


def circumference_area(radius):
    """Returns the area of a circumference"""
    area = math.pi * (radius * radius)
    return round(area, 1)

if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.square = 4
            self.rectangle = 8
            self.triangle = 25
            self.rhombus = 8.1
            self.trapezoid = 36
            self.polygon = 168
            self.circumference = 706.9

        def test_square_area(self):
            side = 2
            self.assertEqual(self.square, square_area(side))

        def test_rectangle_area(self):
            base = 2
            height = 4
            self.assertEqual(self.rectangle, rectangle_area(base, height))

        def test_triangle_area(self):
            base = 5
            height = 10
            self.assertEqual(self.triangle, triangle_area(base, height))

        def test_rhombus_area(self):
            diagonal_1 = 3
            diagonal_2 = 5.4
            self.assertEqual(self.rhombus, rhombus_area(diagonal_1, diagonal_2))

        def test_trapezoid_area(self):
            base_minor = 6
            base_major = 12
            height = 4
            self.assertEqual(self.trapezoid, trapezoid_area(base_minor, base_major, height))

        def test_regular_polygon_area(self):
            perimeter = 48
            apothem = 7
            self.assertEqual(self.polygon, regular_polygon_area(perimeter, apothem))

        def test_circumference_area(self):
            radio = 15
            self.assertEqual(self.circumference, circumference_area(radio))

        def tearDown(self):
            del(self.square)
            del(self.rectangle)
            del(self.triangle)
            del(self.rhombus)
            del(self.polygon)
            del(self.circumference)

    unittest.main()

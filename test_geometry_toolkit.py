# test_geometry_toolkit.py

from geometry_toolkit import Coordinate
import math


# ------ TESTING POINT METHODS ------
p1 = Coordinate(2, 3)
p2 = Coordinate(-4, 7)
p3 = Coordinate(5, -6)

# __str__ method
assert str(p1) == "(2,3)"
assert str(p2) == "(-4,7)"

# Reflection methods
assert p1.reflect_over_x_axis().__str__() == "(2,-3)"
assert p1.reflect_over_y_axis().__str__() == "(-2,3)"
assert p1.reflect_about_origin().__str__() == "(-2,-3)"

# ------ TWO POINT OPERATIONS ------
# Distance
assert p1.distance_between_two_point(p2) == round(((2+4)**2 + (3-7)**2)**0.5, 2)

# Midpoint
mid = p1.midpoint_of_two_points(p2)
assert mid.x == -1.0 and mid.y == 5.0

# Slope
assert p1.slope_of_line_joining_two_point(p2) == round((7-3)/(-4-2), 2)

# Equation of line
assert isinstance(p1.equation_of_line_joining_two_point(p2), str)

# ------ THREE POINT OPERATIONS ------
assert isinstance(p1.area_of_triangle_formed_by_given_three_points(p2, p3), str)
assert isinstance(p1.type_of_triangle_formed_by_given_three_points(p2, p3), str)
assert isinstance(p1.perimeter_of_triangle_formed_by_given_three_points(p2, p3), float)
assert p1.is_colinear_given_three_points(p2, p3) in [True, False]
assert p1.is_right_angle_trangle_formed_by_given_three_points(p2, p3) in ["YES", "NO"]

# Triangle centers
assert isinstance(p1.centroid_of_traingle_formed_by_given_three_points(p2, p3), Coordinate)
assert isinstance(p1.incentre_of_triangle_formed_by_given_three_points(p2, p3), (Coordinate, str))
assert isinstance(p1.circumcentre_of_triangle_given_three_points(p2, p3), (Coordinate, str))
assert isinstance(p1.orthocentre_of_triangle_given_three_points(p2, p3), (Coordinate, str))

# ------ INTERSECTION (INTERNAL/EXTERNAL DIVISION) ------
assert isinstance(p1.internal_division_of_line_joining_two_points(p2, "1:2"), Coordinate)
assert isinstance(p1.external_division_of_line_joining_two_points(p2, "3:1"), Coordinate)

# ------ LINE EQUATION METHODS ------
# Using Point and Slope
assert isinstance(p1.equation_of_line_given_point_and_slope("2"), str)
assert isinstance(p1.equation_of_line_given_point_and_slope("0"), str)
assert isinstance(p1.equation_of_line_given_point_and_slope("Undefined"), str)

# ------ LINE AND POINT METHODS ------
line = "2x+3y-6=0"
assert isinstance(p1.distance_between_given_point_and_line(line), float)
assert p1.is_point_lies_on_line("2x+3y-13=0") in [True, False]
assert isinstance(p1.image_of_point_in_given_line(line), Coordinate)
assert isinstance(p1.foot_of_perpendicular_of_point_in_given_line(line), Coordinate)

# ------ STATIC METHODS: LINE ------
assert Coordinate.standardize_line_equation("2x+3y=6") == "2x+3y-6=0"
assert Coordinate.extracting_the_cofficient_from_equation_of_line("2x+3y=6") == (2.0, 3.0, -6.0)

assert math.isclose(Coordinate.extracting_slope_from_line("2x+3y=6"),  -2.0 / 3.0,rel_tol=1e-2)
assert Coordinate.is_parallel_lines("2x+3y=6", "4x+6y=12") is True
assert Coordinate.is_perpendicular_lines("2x+3y=6", "3x-2y=7") is True
assert Coordinate.is_intersecting_lines("x+y=4", "x-y=2") is True
assert isinstance(Coordinate.point_of_intersection_of_two_line("x+y=4", "x-y=2"), Coordinate)

# ------ BUNDLED METHODS ------
assert isinstance(p1.calculation_for_single_point(), str)
assert isinstance(p1.calculation_for_two_points(p2), str)
assert isinstance(p1.calculation_for_three_points(p2, p3), str)
assert isinstance(p1.calculation_for_line_and_point(line), str)
assert isinstance(Coordinate.calculation_for_single_line("2x+3y=6"), str)
assert isinstance(Coordinate.calculation_for_two_line("x+y=4", "x-y=2"), str)
assert isinstance(p1.calculation_for_intersection_for_two_point(p2, "2:3"), str)

print("All tests passed successfully!")
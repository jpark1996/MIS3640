"""
Write a definition for a class named Circle with attributes center and radius , where
center is a Point object and radius is a number.
Instantiate a Circle object that represents a circle with its center at 150, 100 and
radius 75.
Write a function named point_in_circle that takes a Circle and a Point and returns
True if the Point lies in or on the boundary of the circle.
Write a function named rect_in_circle that takes a Circle and a Rectangle and
returns True if the Rectangle lies entirely in or on the boundary of the circle.
Write a function named rect_circle_overlap that takes a Circle and a Rectangle
and returns True if any of the corners of the Rectangle fall inside the circle. Or as a
more challenging version, return True if any part of the Rectangle falls inside the
circle.
"""
import copy
from math import sqrt


class Point:
    """Represents a point in 2-D space."""


class Rectangle:
    """Represents a rectangle.
    Attributes: width, height, corner.
    """


class Circle:
    """Represents a circle.
    Attributes: center, radius.
    """


ring = Circle()
ring.radius = 75.0
ring.center = Point()
ring.center.x = 150.0
ring.center.y = 100.0


def point_in_circle(c, p):
    """Checks if a point lies within, or on the boundary of, a circle.
    c: Circle
    p: Point
    returns: Bool
    """
    dx = p.x - c.center.x
    dy = p.y - c.center.y

    if sqrt(dx**2 + dy**2) <= c.radius:
        return True
    return False


dot = Point()
dot.x = 170
dot.y = 90

print('point_in_circle (True):', point_in_circle(ring, dot))

dot2 = Point()
dot2.x = 75.0
dot2.y = 25.0

print('point_in_circle (False):', point_in_circle(ring, dot2))

dot3 = Point()
dot3.x = 75.0
dot3.y = 100.0

print('point_in_circle (True):', point_in_circle(ring, dot3))


def get_rect_corners(r):
    """Returns a list of corners for a rectangle
    r: Rectangle
    returns: List of Points
    """
    corners = []

    # Fetch corner of rectangle
    p = r.corner
    # Save corner in list using copy to avoid aliasing
    corners.append(copy.copy(p))
    # Calculate and store each subsequent corner
    p.x += box.width
    corners.append(copy.copy(p))
    p.y = p.y + box.height
    corners.append(copy.copy(p))
    p.x = p.x - box.width
    corners.append(copy.copy(p))

    return corners


def rect_in_circle(r, c):
    """Checks if a rectangle lies entirely within, or on the boundary of,
    a circle.
    r: Rectangle
    c: Circle
    returns: Bool
    """
    corners = get_rect_corners(r)

    # Iterate through corners and check if in circle
    for point in corners:
        if not point_in_circle(c, point):
            return False
    return True


box = Rectangle()
box.height = 1.0
box.width = 1.0
box.corner = Point()
box.corner.x = 75.0
box.corner.y = 25.0

print('rect_in_circle:', rect_in_circle(box, ring))


def rect_circle_overlap(r, c):
    """Checks if any corner of a rectangle lies within, or on the boundary
    of, a circle.
    r: Rectangle
    c: Circle
    returns: Bool
    """
    corners = get_rect_corners(r)

    for point in corners:
        if point_in_circle(c, point):
            return True
    return False


print('rect_circle_overlap:', rect_circle_overlap(box, ring))
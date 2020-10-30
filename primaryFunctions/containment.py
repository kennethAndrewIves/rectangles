from classes.rectangle import Rectangle
from utils.helpers import rotate_point
import math


def rectangle_containment(outerRect: Rectangle, innerRect: Rectangle):
    # determine the angle required to rotate the outerRect to be in line with the x axis
    height = abs(outerRect.c[1] - outerRect.d[1])
    length = abs(outerRect.c[0] - outerRect.d[0])
    theta = math.atan(float(height / length))

    # Rotating just points A and C on the outer rect will give us the bounds for the roated inner rect
    rotated_outer_rect = [
        rotate_point(outerRect.a, theta),
        rotate_point(outerRect.c, theta),
    ]
    rotated_inner_rect = [
        rotate_point(innerRect.a, theta),
        rotate_point(innerRect.b, theta),
        rotate_point(innerRect.c, theta),
        rotate_point(innerRect.d, theta),
    ]

    lower_x_bound = round(rotated_outer_rect[0][0])
    upper_x_bound = round(rotated_outer_rect[1][0])
    lower_y_bound = round(rotated_outer_rect[1][1])
    upper_y_bound = round(rotated_outer_rect[0][1])

    for point in rotated_inner_rect:
        x = round(point[0])
        y = round(point[0])
        if not ((lower_x_bound < x < upper_x_bound) and (lower_y_bound < y < upper_y_bound)):
            return False
    return True

import math
from decimal import Decimal


# calculate the euclidean distance between two points
def distance(point_a: Decimal, point_b: Decimal) -> Decimal:
    distance_squared = (point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2
    return distance_squared.sqrt()


def rotate_point(point, rad):
    # Should just refactor everything to be floats
    x = float(point[0])
    y = float(point[1])
    x_rot = math.cos(rad) * x - math.sin(rad) * y
    y_rot = math.sin(rad) * x + math.cos(rad) * y
    return x_rot, y_rot

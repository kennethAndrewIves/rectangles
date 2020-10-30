from decimal import Decimal
from classes.linesegment import LineSegment
from utils.helpers import distance

class Rectangle:
    def __init__(self, corner1, corner2, corner3, corner4):
        # Using decimal to maintain precision
        corner1 = Decimal(corner1[0]), Decimal(corner1[1])
        corner2 = Decimal(corner2[0]), Decimal(corner2[1])
        corner3 = Decimal(corner3[0]), Decimal(corner3[1])
        corner4 = Decimal(corner4[0]), Decimal(corner4[1])
        unordered_corners = [corner1, corner2, corner3, corner4]

        # corner a is the corner the furthest to the left, if another corner is on the same x coordinate, the higher
        # corner should be taken. See readme for details on rectangle corners.
        corner_a_index = 0
        for i in range(1, len(unordered_corners)):
            if (unordered_corners[i][0] <= unordered_corners[corner_a_index][0]
                    and unordered_corners[i][1] >= unordered_corners[corner_a_index][1]):
                corner_a_index = i
        self.a = unordered_corners[corner_a_index]
        del unordered_corners[corner_a_index]

        # corner c is the corner the furthest from corner a
        corner_c_index = 0
        for i in range(1, len(unordered_corners)):
            if distance(self.a, unordered_corners[i]) > distance(self.a, unordered_corners[corner_c_index]):
                corner_c_index = i
        self.c = unordered_corners[corner_c_index]
        del unordered_corners[corner_c_index]

        # corner b should be to the right of corner a, the remaining corner is corner d
        if unordered_corners[0][0] > self.a[0]:
            self.b = unordered_corners[0]
            self.d = unordered_corners[1]
        else:
            self.b = unordered_corners[1]
            self.d = unordered_corners[0]

        # have to validate that the rectangle is indeed a rectangle
        # parallel sides must be equal distance
        distance_a_b = distance(self.a, self.b)
        distance_a_d = distance(self.a, self.d)
        distance_c_b = distance(self.c, self.b)
        distance_c_d = distance(self.c, self.d)
        self.valid = (round(distance_a_b, 5) == round(distance_c_d, 5)) and (
                    round(distance_a_d, 5) == round(distance_c_b, 5))
        # if the squared distance between a and c is equal to the sum of the other two sides, the shape can be cut in
        # two form two right triangles, and is therefore a valid rectangle.
        if self.valid:
            distance_a_c = distance(self.a, self.c)
            self.valid = round((distance_a_c ** 2), 5) == round((distance_a_b ** 2 + distance_a_d ** 2), 5)

        # generate line segments that will be helpful for calculating intersections
        if self.valid:
            self.lines = [LineSegment(self.a, self.b),
                          LineSegment(self.a, self.d),
                          LineSegment(self.c, self.b),
                          LineSegment(self.c, self.d)]




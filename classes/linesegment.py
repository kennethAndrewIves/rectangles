from decimal import Decimal
from utils.enums import Adjacency


class LineSegment:
    def __init__(self, point1: Decimal, point2: Decimal):
        # Slope of a line segment is the rise/run. If run is 0, slope is infinite and represented by 1.
        if point2[0] != point1[0]:
            self.slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
        else:
            self.slope = None

        # intercept is where the line crosses the y axis. If the slope is infinite, it will be where the line crosses
        # the x axis
        if self.slope is None:
            self.intercept = point1[0]
        else:
            self.intercept = point1[1] - (self.slope * point1[0])

        # interval of a line segment is the x coords it exists on. If the slope is infinite, the interval will be range
        # of y coords instead.
        if self.slope is None:
            self.interval = min(point1[1], point2[1]), max(point1[1], point2[1])
        else:
            self.interval = min(point1[0], point2[0]), max(point1[0], point2[0])

    def intersection_check(self, line):
        # check if they are parallel lines, if they are, no intersection exists
        if self.slope == line.slope:
            return None
        # check if one of the lines is vertical, this requires different intersection logic
        elif self.slope is None or line.slope is None:
            if self.slope is None:
                vertical_line = self
                other_line = line
            else:
                vertical_line = line
                other_line = self
            y_intersection = other_line.slope * vertical_line.intercept + other_line.intercept
            # check if intersection occurs in the range of both lines
            if (vertical_line.interval[0] <= y_intersection <= vertical_line.interval[1] and
                    other_line.interval[0] <= vertical_line.intercept <= other_line.interval[1]):
                return round(vertical_line.intercept, 5), round(y_intersection, 5)
            else:
                return None
        else:
            x_intersection = (line.intercept - self.intercept) / (self.slope - line.slope)
            y_intersection = self.slope * x_intersection + self.intercept
            #  check if intersection occurs in the range of both lines
            if (self.interval[0] < round(x_intersection, 5) < self.interval[1] and
                    line.interval[0] < round(x_intersection, 5) < line.interval[1]):
                return round(x_intersection, 5), round(y_intersection, 5)
            else:
                return None

    def adjacency_check(self, line):
        # if the lines are the same
        if round(self.slope, 5) == round(line.slope, 5) and round(self.intercept, 5) == round(line.intercept, 5):
            # check to see over what range the lines overlap to determine if there's adjacency and what if so what type
            if self.interval[0] == line.interval[0] and self.interval[1] == line.interval[1]:
                return True, Adjacency.Proper
            elif self.interval[0] < line.interval[0] and self.interval[1] > line.interval[1]:
                return True, Adjacency.PrimarySubline
            elif line.interval[0] < self.interval[0] and line.interval[1] > self.interval[1]:
                return True, Adjacency.SecondarySubline
            elif (line.interval[0] < self.interval[0] < line.interval[1] or
                  self.interval[0] < line.interval[0] < self.interval[1]):
                return True, Adjacency.Partial
            else:
                return False
        else:
            return False

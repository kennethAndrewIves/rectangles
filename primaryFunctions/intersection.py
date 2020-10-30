from classes.rectangle import Rectangle
from primaryFunctions.adjacency import rectangle_adjacency
from utils.enums import Adjacency

def rectangle_intersection(rect1: Rectangle, rect2: Rectangle):
    # there can be no intersections if the rectangles are properly adjacent
    adjacent = rectangle_adjacency(rect1, rect2)
    if adjacent and adjacent[1] == Adjacency.Proper:
        return None
    intersection_set = set()
    for line1 in rect1.lines:
        for line2 in rect2.lines:
            intersection = line1.intersection_check(line2)
            if (intersection is not None) and (intersection not in intersection_set):
                intersection_set.add(intersection)
    if not intersection_set:
        return None
    else:
        intersection_list = []
        for intersection in intersection_set:
            intersection_list.append(intersection)
        return intersection_list



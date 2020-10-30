# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from classes.rectangle import Rectangle
from primaryFunctions.intersection import rectangle_intersection
from primaryFunctions.adjacency import rectangle_adjacency
from primaryFunctions.containment import rectangle_containment

def check_rectangle(a, b, c, d, e, f, g, h):
    rect1 = Rectangle(a, b, c, d)
    rect2 = Rectangle(e, f, g, h)
    if rect1.valid and rect2.valid:
        intersections = rectangle_intersection(rect1, rect2)
        if intersections:
            for intersection in intersections:
                print(intersection)
        else:
            print("no intersections")

        rect_adjacency = rectangle_adjacency(rect1, rect2)
        print(rect_adjacency)

        print(rectangle_containment(rect1, rect2))
    else:
        print("invalid entry")


if __name__ == "__main__":
    a = float(sys.argv[1]), float(sys.argv[2])
    b = float(sys.argv[3]), float(sys.argv[4])
    c = float(sys.argv[5]), float(sys.argv[6])
    d = float(sys.argv[7]), float(sys.argv[8])
    e = float(sys.argv[9]), float(sys.argv[10])
    f = float(sys.argv[11]), float(sys.argv[12])
    g = float(sys.argv[13]), float(sys.argv[14])
    h = float(sys.argv[15]), float(sys.argv[16])
    check_rectangle(a, b, c, d, e, f, g, h)

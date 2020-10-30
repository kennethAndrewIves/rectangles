from classes.rectangle import Rectangle

def rectangle_adjacency(rect1: Rectangle, rect2: Rectangle):
    for line1 in rect1.lines:
        for line2 in rect2.lines:
            adjacency = line1.adjacency_check(line2)
            if adjacency:
                return adjacency
    return False


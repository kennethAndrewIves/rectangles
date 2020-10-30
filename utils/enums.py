import enum


class Adjacency(enum.Enum):
    Proper = 1
    # Primary Subline means the linesegment class being called contains the second linesegment
    PrimarySubline = 2
    # Secondary Subline means the linesegment class being called is contained within the second linesegment
    SecondarySubline = 3
    Partial = 4
    NonAdjacent = 5

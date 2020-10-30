# Rectangles
The Rectangles repository can take 2 sets of 4 points. It will validate if the set of points is a rectangle in euclidean space. Then it will perform 3 operations on the 2 rectangles, intersection, adjacency, and containment. 

The intersection function will return all the points that the two rectangles have intersections at. 

The adjacency function will return if the two rectangles are adjacent, and if so what type. 

The containment function will check if the second rectangle fits entirely within the first.  

## How To Run
Pull the repo, ensure you are running a computer with python 3 installed. There is no need to install additional dependencies. Open a terminal in the main directory and run the following command

python3 main.py ax ay bx by cx xy dx dy ex ey fx fy gx gy hx hy

but subtitute the vertices of your rectangles in place of ax, ay, etc. The first 4 points make up the first rectangle, the second four points make up the second rectangle. X coordinate always comes first, followed by the Y coordinate. 

The testcases.txt has some examples of test commands you can run on various rectangles in different situations. 

The output will be:
[intersections if any]
[true/false] for adjacency
[true/false] for containment

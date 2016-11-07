import math
from Simple import Vector

class VectorField(Vector.Vector):
    def __init__(self, point, contour_point):
        #print("x1 = {0}, x2 = {1}".format(point, contour_point))

        if point == contour_point:
            self.x = 0
            self.y = 0
        else:
            den = ((point.x - contour_point.x) ** 2 + (point.y - contour_point.y) ** 2) ** 0.5
            self.x = (contour_point.y - point.y) / (math.pi * den)
            self.y = (point.x - contour_point.x) / (math.pi * den)


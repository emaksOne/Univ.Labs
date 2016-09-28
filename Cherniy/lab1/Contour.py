from Simple import Point

class Contour:
    def __init__(self, list_of_points):

        #вихрь
        self.list_of_vortex = list_of_points;
        self.list_of_callocation_points = self.FindCallocationPoints()

    def FindCallocationPoints(self):
        temp = []
        for i in range(0, len(self.list_of_vortex)-1):
            x1 = (self.list_of_vortex[i].x + self.list_of_vortex[i+1].x)/2
            x2 = (self.list_of_vortex[i].y + self.list_of_vortex[i+1].y)/2
            temp.append(Point.Point(x1, x2))
        return temp
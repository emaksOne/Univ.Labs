class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def CreateListOfPoints(data):
    points = []
    for i in range(0, len(data)):
        point = Point(data[i][0], data[i][1])
        points.append(point)
    return points
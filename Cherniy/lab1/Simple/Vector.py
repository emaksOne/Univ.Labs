from Simple import Point

class Vector:
    x = 0
    y = 0

    def __init__(self, point):
        self.x = point.x
        self.y = point.y

    def __init__(self, x = 0, y =0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x*other.x + self.y*other.y
        else:
            x = self.x * other
            y = self.y * other
            return Vector(x, y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return self.x == other and self.y == other.y


from Simple import Vector


class Normal(Vector.Vector):
    def __init__(self, point1, point2):
        norm = ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5
        x2 = (point2.x - point1.x) / norm
        x1 = (-1) * (point2.y - point1.y) / norm
        self.x = x1
        self.y = x2


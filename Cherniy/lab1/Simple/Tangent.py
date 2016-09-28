from Simple import Vector


class Tangent(Vector):
    def __init__(self, point1, point2):
        norm = ((point2.x - point1.x)**2 + (point2.y - point1.y)**2) ** 0.5
        x1 = (point2.x - point1.x) / norm
        x2 = (point2.y - point1.y) / norm
        self.x = x1
        self.y = x2

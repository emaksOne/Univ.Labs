import numpy as np
from Simple import Point
def parsePoints(points):
    res = []
    res.append([])
    res.append([])

    for p in points:
        res[0].append(p.x)
        res[1].append(p.y)
    return res

def parseContour(points):
    res = []
    for i in range(0, len(points) - 1):
        line = {
            'x0': points[i].x,
            'y0': points[i].y,
            'x1': points[i+1].x,
            'y1': points[i+1].y
        }
        res.append(line)
    return res


def parseField(field):
    res = []
    for i in range(0, len(field), 2):               #for i in range(0, len(field), 2):
        for j in range(0, len(field[0]), 3):        #for j in range(0, len(field[0]), 2):
           line = {
               'x0': i,
               'y0': j,
               'x1': i + field[i][j].x,
               'y1': j + field[i][j].y
           }
           res.append(line)
    return res

def createContour():
    points = []
    x_up = np.arange(31, 17, -0.5)
    print(x_up)
    print('len(x) = {0}'.format(len(x_up)))
    y_up = []
    for i in x_up:
        temp = 5.0 / 4.0 * ((- i ** 2 + 50 * i - 561) ** 0.5 + 20)
        points.append(Point.Point(i, temp))
        y_up.append(temp)
    print(y_up)
    print('len(y_up) = {0}'.format(len(y_up)))

    x_down = np.arange(17, 31, 0.5)
    y_down = []
    for i in x_down:
        temp = 5.0 / 4.0 * (20 - (- i ** 2 + 50 * i - 561) ** 0.5)
        points.append(Point.Point(i, temp))
        y_down.append(temp)
    print(y_down)
    print('len(y_down) = {0}'.format(len(y_down)))

    return points
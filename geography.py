import math


def coordinate(x1, y1, d, corner):
    x2 = int(x1) + int(d) * math.cos(int(corner))
    y2 = int(y1) + int(d) * math.sin(int(corner))
    return x2, y2

def distance(x1, x2 ,y1 ,y2):
    d = math.sqrt((int(x2) - int(x1)**2 + (int(y2) - int(y1))**2))
    return d

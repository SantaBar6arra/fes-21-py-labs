import math


def ab_distance(a, b):
    """Return the distance between two points (ax, ay) and (bx, by)."""
    ax, ay = a
    bx, by = b
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
from itertools import combinations
from math import sqrt

pairs = []
points = []
best = 0


def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def distance(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def is_between(a, c, b):
    return distance(a, c) + distance(c, b) == distance(a, b)


def line_segment_intersection(polygon, point):

    inside = False
    num_vertices = len(polygon)
    x, y = point
    for i in range(num_vertices):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % num_vertices]
        if is_between((x1, y1), point, (x2, y2)):
            return True
        if (y1 > y) != (y2 > y) and x < x1 + ((y - y1) * (x2 - x1) / (y2 - y1)):
            inside = not inside
    return inside


with open("2025/input/day09") as f:
    data = f.read().splitlines()

    for line in data:
        x = tuple(int(x) for x in line.split(","))
        points.append(x)

for p1, p2 in combinations(points, 2):
    surface = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
    if surface > best:
        best = surface


print(f"Partie 1 : {best}")

best = 0

for p1, p2 in combinations(points, 2):

    surface = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
    if surface <= best:
        continue
    potential = True

    edges = [
        (p1, (p1[0], p2[1])),
        ((p1[0], p2[1]), p2),
        (p2, (p2[0], p1[1])),
        ((p2[0], p1[1]), p1),
    ]

    for edge in edges:
        intersections = 0
        p_edge1 = min(edge)
        p_edge2 = max(edge)
        if p_edge1[0] != p_edge2[0]:
            p_edge1 = (p_edge1[0] + 1, p_edge1[1])
            p_edge2 = (p_edge2[0] - 1, p_edge2[1])
        else:
            p_edge1 = (p_edge1[0], p_edge1[1] + 1)
            p_edge2 = (p_edge2[0], p_edge2[1] - 1)
        if potential:
            i = 0
            inter = 0
            intersections += sum(
                [
                    1
                    for i in range(len(points))
                    if intersect(
                        p_edge1, p_edge2, points[i], points[(i + 1) % len(points)]
                    )
                ]
            )
            if intersections > 1 or not (
                line_segment_intersection(points, p_edge1)
                and line_segment_intersection(points, p_edge2)
            ):
                potential = False

    if potential:
        best = surface

print(f"Partie 2 : {best}")

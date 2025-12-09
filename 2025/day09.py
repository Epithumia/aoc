from itertools import combinations
from shapely.geometry import Point, Polygon, LineString
from shapely import prepare

pairs = []
points = []
best = 0

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

area = Polygon([Point(x) for x in points])
prepare(area)
best = 0

for p1, p2 in combinations(points, 2):
    surface = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
    if surface <= best:
        continue
    rect_points = [
        Point(p1),
        Point(p1[0], p2[1]),
        Point(p2),
        Point(p2[0], p1[1]),
    ]
    rect = LineString(rect_points)
    if area.contains(rect):
        best = surface

print(f"Partie 2 : {best}")

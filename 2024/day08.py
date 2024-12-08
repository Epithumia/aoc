from collections import defaultdict
from itertools import combinations

antennas = defaultdict(lambda: list())
anti_nodes = set()
h = 0
w = 0

with open("2024/input/day08") as f:
    data = f.read().splitlines()

    h = len(data)
    w = len(data[0])

    for x in range(h):
        for y in range(w):
            if data[x][y] != ".":
                antennas[data[x][y]].append((x, y))

for antenna in antennas.keys():
    coords = antennas[antenna]
    for c in combinations(coords, 2):
        dx = c[0][0] - c[1][0]
        dy = c[0][1] - c[1][1]
        if (c[0][0] + dx, c[0][1] + dy) != c[1] and (
            0 <= c[0][0] + dx < w and 0 <= c[0][1] + dy < h
        ):
            anti_nodes.add((c[0][0] + dx, c[0][1] + dy))
        if (c[0][0] - dx, c[0][1] - dy) != c[1] and (
            0 <= c[0][0] - dx < w and 0 <= c[0][1] - dy < h
        ):
            anti_nodes.add((c[0][0] - dx, c[0][1] - dy))
        if (c[1][0] + dx, c[1][1] + dy) != c[0] and (
            0 <= c[1][0] + dx < w and 0 <= c[1][1] + dy < h
        ):
            anti_nodes.add((c[1][0] + dx, c[1][1] + dy))
        if (c[1][0] - dx, c[1][1] - dy) != c[0] and (
            0 <= c[1][0] - dx < w and 0 <= c[1][1] - dy < h
        ):
            anti_nodes.add((c[1][0] - dx, c[1][1] - dy))

print("Part 1:", len(anti_nodes))

anti_nodes = set()

for antenna in antennas.keys():
    coords = antennas[antenna]
    for c in combinations(coords, 2):
        dx = c[0][0] - c[1][0]
        dy = c[0][1] - c[1][1]
        for k in range(max(h // abs(dx), w // abs(dy))):
            if 0 <= c[0][0] + k * dx < w and 0 <= c[0][1] + k * dy < h:
                anti_nodes.add((c[0][0] + k * dx, c[0][1] + k * dy))
            if 0 <= c[0][0] - k * dx < w and 0 <= c[0][1] - k * dy < h:
                anti_nodes.add((c[0][0] - k * dx, c[0][1] - k * dy))
            if 0 <= c[1][0] + k * dx < w and 0 <= c[1][1] + k * dy < h:
                anti_nodes.add((c[1][0] + k * dx, c[1][1] + k * dy))
            if 0 <= c[1][0] - k * dx < w and 0 <= c[1][1] - k * dy < h:
                anti_nodes.add((c[1][0] - k * dx, c[1][1] - k * dy))

print("Part 2:", len(anti_nodes))

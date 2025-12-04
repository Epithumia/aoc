from collections import defaultdict


def accessible(floor_map, coord):
    if floor_map[coord] == ".":
        return False
    neighbors = sum(
        [
            1
            for n in [
                (coord[0] - 1, coord[1]),
                (coord[0] + 1, coord[1]),
                (coord[0], coord[1] - 1),
                (coord[0], coord[1] + 1),
                (coord[0] - 1, coord[1] - 1),
                (coord[0] - 1, coord[1] + 1),
                (coord[0] + 1, coord[1] - 1),
                (coord[0] + 1, coord[1] + 1),
            ]
            if floor_map[n] == "@"
        ]
    )
    if neighbors >= 4:
        return False
    return True


floor_map = defaultdict(lambda: ".")


with open("2025/input/day04") as f:
    data = [list(row) for row in f.read().splitlines()]
    rows = len(data)
    cols = len(data[0])
    for i in range(rows):
        for j in range(cols):
            floor_map[i, j] = data[i][j]

partie1 = sum(
    [1 for i in range(rows) for j in range(cols) if accessible(floor_map, (i, j))]
)

print("Partie 1:", partie1)

flagged = set()
updated = True
while updated:
    updated = False
    for i in range(rows):
        for j in range(cols):
            if accessible(floor_map, (i, j)):
                flagged.add((i, j))
                updated = True
    for f in flagged:
        floor_map[f] = "."

print("Partie 2:", len(flagged))

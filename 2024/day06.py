from collections import defaultdict
from tqdm import tqdm


def move_guard(lab_map, x, y):
    dx = {"^": -1, ">": 0, "v": 1, "<": 0}
    dy = {"^": 0, ">": 1, "v": 0, "<": -1}
    turn = {"^": ">", ">": "v", "v": "<", "<": "^"}
    orientation = lab_map[x, y]
    if lab_map[x + dx[orientation], y + dy[orientation]] in [".", "X"]:
        lab_map[x, y] = "X"
        lab_map[x + dx[orientation], y + dy[orientation]] = orientation
        return (x + dx[orientation], y + dy[orientation])
    if lab_map[x + dx[orientation], y + dy[orientation]] == "*":
        lab_map[x, y] = "X"
        return (None, None)
    lab_map[x, y] = turn[orientation]
    return (x, y)


lab_map = defaultdict(lambda: "*")
start = None
h = 0
w = 0

with open("2024/input/day06") as f:
    data = f.read().splitlines()

    h = len(data)
    w = len(data[0])
    for i in range(len(data)):
        for j in range(len(data[0])):
            lab_map[i, j] = data[i][j]
            if data[i][j] in ["^", "v", "<", ">"]:
                start = (i, j)

pos = start
while pos[0] is not None:
    pos = move_guard(lab_map, pos[0], pos[1])

interest = []

nb_pos = 0
for i in range(h):
    for j in range(w):
        if lab_map[i, j] == "X":
            nb_pos += 1
            interest.append((i, j))

print("Part 1:", nb_pos)

nb_obs = 0

for tx, ty in tqdm(interest):
    # load the map again
    for i in range(len(data)):
        for j in range(len(data[0])):
            lab_map[i, j] = data[i][j]
            if data[i][j] in ["^", "v", "<", ">"]:
                start = (i, j)
    path = []
    if lab_map[tx, ty] != "#" and (tx, ty) != start:
        lab_map[tx, ty] = "#"
        pos = start
        path = [(None, None, pos[0], pos[1])]
        stop = False
        while pos[0] is not None and not stop:
            pos = move_guard(lab_map, pos[0], pos[1])
            prev = path[-1]
            if (prev[2], prev[3], pos[0], pos[1]) not in path[:-1] and pos[
                0
            ] is not None:
                path.append((prev[2], prev[3], pos[0], pos[1]))
            elif pos[0] is not None:
                stop = True
        if stop:
            nb_obs += 1

print("Part 2:", nb_obs)

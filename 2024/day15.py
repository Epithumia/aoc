from collections import defaultdict

warehouse = defaultdict(lambda: ".")
moves = []
robot = None
h = 0
w = 0


def draw_warehouse(warehouse):
    for i in range(h):
        for j in range(w):
            print(warehouse[(i, j)], end="")
        print()


def move(x, y, direction, warehouse):
    dx = {"^": -1, ">": 0, "v": 1, "<": 0}
    dy = {"^": 0, ">": 1, "v": 0, "<": -1}
    if warehouse[(x + dx[direction], y + dy[direction])] == "#":
        return False
    if warehouse[(x + dx[direction], y + dy[direction])] == ".":
        warehouse[(x + dx[direction], y + dy[direction])] = warehouse[(x, y)]
        warehouse[(x, y)] = "."
        return True
    if warehouse[(x + dx[direction], y + dy[direction])] == "O":
        if move(x + dx[direction], y + dy[direction], direction, warehouse):
            warehouse[(x + dx[direction], y + dy[direction])] = warehouse[(x, y)]
            warehouse[(x, y)] = "."
            return True
    return False


def wide_move(x, y, direction, warehouse):
    dx = {"^": -1, ">": 0, "v": 1, "<": 0}
    dy = {"^": 0, ">": 1, "v": 0, "<": -1}
    if warehouse[(x, y)] == "#":
        return False
    if direction in ["<", ">"]:
        if warehouse[(x + dx[direction], y + dy[direction])] == "#":
            return False
        if warehouse[(x + dx[direction], y + dy[direction])] == ".":
            warehouse[(x + dx[direction], y + dy[direction])] = warehouse[(x, y)]
            warehouse[(x, y)] = "."
            return True
        if warehouse[(x + dx[direction], y + dy[direction])] in ["[", "]"]:
            if wide_move(x + dx[direction], y + dy[direction], direction, warehouse):
                warehouse[(x + dx[direction], y + dy[direction])] = warehouse[(x, y)]
                warehouse[(x, y)] = "."
                return True
        return False
    if warehouse[(x + dx[direction], y + dy[direction])] == "#":
        return False
    if warehouse[(x + dx[direction], y + dy[direction])] == ".":
        warehouse[(x + dx[direction], y + dy[direction])] = warehouse[(x, y)]
        warehouse[(x, y)] = "."
        return True
    if warehouse[(x + dx[direction], y + dy[direction])] == "[":
        if wide_move(
            x + dx[direction], y + dy[direction], direction, warehouse
        ) and wide_move(x + dx[direction], y + dy[direction] + 1, direction, warehouse):
            warehouse[(x + dx[direction], y + dy[direction])] = warehouse[(x, y)]
            warehouse[(x, y)] = "."
            return True
        return False
    if warehouse[(x + dx[direction], y + dy[direction])] == "]":
        if wide_move(
            x + dx[direction], y + dy[direction], direction, warehouse
        ) and wide_move(x + dx[direction], y + dy[direction] - 1, direction, warehouse):
            warehouse[(x + dx[direction], y + dy[direction])] = warehouse[(x, y)]
            warehouse[(x, y)] = "."
            return True
        return False
    return False


def gps(warehouse):
    return sum([100 * x + y for x, y in warehouse if warehouse[(x, y)] in ["O", "["]])


def wide_gps(warehouse):
    return sum([100 * x + y for x, y in warehouse if warehouse[(x, y)] == "["])


with open("2024/input/day15") as f:
    data = f.read().splitlines()

    i = 0
    for line in data:
        if line and line[0] == "#":
            w = len(line)
            for j in range(len(line)):
                warehouse[i, j] = line[j]
                if line[j] == "@":
                    robot = (i, j)
            i += 1

        elif line and line[0] in ["^", "<", ">", "v"]:
            for m in line:
                moves.append(m)

        h = i


for m in moves:
    has_moved = move(robot[0], robot[1], m, warehouse)
    if has_moved:
        if m == "^":
            robot = (robot[0] - 1, robot[1])
        elif m == ">":
            robot = (robot[0], robot[1] + 1)
        elif m == "v":
            robot = (robot[0] + 1, robot[1])
        elif m == "<":
            robot = (robot[0], robot[1] - 1)

print("Part 1:", gps(warehouse))

warehouse = defaultdict(lambda: ".")
moves = []

with open("2024/input/day15") as f:
    data = f.read().splitlines()

    i = 0
    for line in data:
        if line and line[0] == "#":
            w = 2 * len(line)
            j = 0
            for p in line:
                if p == "@":
                    robot = (i, j)
                    warehouse[i, j] = "@"
                    warehouse[i, j + 1] = "."
                elif p == "O":
                    warehouse[i, j] = "["
                    warehouse[i, j + 1] = "]"
                else:
                    warehouse[i, j] = p
                    warehouse[i, j + 1] = p
                j += 2
            i += 1

        elif line and line[0] in ["^", "<", ">", "v"]:
            for m in line:
                moves.append(m)

        h = i

for m in moves:
    wh = warehouse.copy()
    has_moved = wide_move(robot[0], robot[1], m, warehouse)
    if has_moved:
        if m == "^":
            robot = (robot[0] - 1, robot[1])
        elif m == ">":
            robot = (robot[0], robot[1] + 1)
        elif m == "v":
            robot = (robot[0] + 1, robot[1])
        elif m == "<":
            robot = (robot[0], robot[1] - 1)
    else:
        warehouse = wh

print("Part 2:", gps(warehouse))

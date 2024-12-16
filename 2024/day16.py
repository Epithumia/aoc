from collections import defaultdict, deque
from math import inf
import heapq

moves = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}


def move(a, b):
    if a[2] == b[2]:
        return 1
    if a[2] == ">" and b[2] in ["v", "^"]:
        return 1001
    if a[2] == "<" and b[2] in ["v", "^"]:
        return 1001
    if a[2] == "v" and b[2] in [">", "<"]:
        return 1001
    if a[2] == "^" and b[2] in [">", "<"]:
        return 1001
    return inf


def dijkstra(graph, source, destination):
    seen = defaultdict(lambda: False)
    bag = []
    heapq.heappush(bag, (0, source, None))
    while len(bag) > 0:
        distance, current, parent = heapq.heappop(bag)
        if current in destination:
            seen[current] = parent
            return distance, seen
        if not seen[current]:
            seen[current] = parent
            neighbors = []
            for turn in [">", "<", "^", "v"]:
                v = (
                    current[0] + moves[turn][0],
                    current[1] + moves[turn][1],
                    turn,
                )
                if graph[v] != "#":
                    neighbors.append(v)
            for neighbor in neighbors:
                cost = move(current, neighbor)
                heapq.heappush(
                    bag,
                    (cost + distance, neighbor, current),
                )
    return inf, None


def potential_points(seen, end):
    potential = set()
    for s in end:
        while True:
            if s is not None:
                potential.add((s[0], s[1]))
                if s in seen.keys():
                    s = seen[s]
                else:
                    break
            else:
                break
    return potential


def point_filter(graphe, point, depth=1):
    next = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    nb = 0
    if not depth:
        return sum(
            [
                (
                    1
                    if graphe[(point[0] + move[0], point[1] + move[1], point[2])] != "#"
                    else 0
                )
                for move in next
            ]
        )
    else:
        return sum(
            [
                (
                    1
                    if point_filter(
                        graphe, (point[0] + move[0], point[1] + move[1], point[2]), 0
                    )
                    > 2
                    else 0
                )
                for move in next
            ]
        )


with open("2024/input/day16") as f:
    data = f.read().splitlines()
    maze = defaultdict(lambda: "#")
    h = len(data)
    w = len(data[0])
    for i in range(h):
        for j in range(w):
            if data[i][j] in [".", "E"]:
                maze[(i, j, ">")] = data[i][j]
                maze[(i, j, "<")] = data[i][j]
                maze[(i, j, "v")] = data[i][j]
                maze[(i, j, "^")] = data[i][j]
                if data[i][j] == "E":
                    end = [(i, j, ">"), (i, j, "<"), (i, j, "v"), (i, j, "^")]
            elif data[i][j] == "S":
                maze[(i, j, ">")] = "S"
                start = (i, j, ">")

cost, seen = dijkstra(maze, start, end)
print("Part 1:", cost)

potential = potential_points(seen, end)
queue = [
    p
    for p in potential
    if any([point_filter(maze, (p[0], p[1], d)) >= 2 for d in [">", "<", "^", "v"]])
]
points = set(p for p in potential)
while len(queue) > 0:
    p = queue.pop()
    c_maze = maze.copy()
    for d in [">", "<", "^", "v"]:
        c_maze[(p[0], p[1], d)] = "#"
    c_cost, seen = dijkstra(c_maze, start, end)

    if c_cost == cost:
        potential = potential_points(seen, end)
        for s in potential:
            points.add((s[0], s[1]))
    else:
        points.add(p)

print("Part 2:", len(points))

import heapq
from collections import defaultdict
from math import inf

def dijkstra(graph, source, destination):
    seen = defaultdict(lambda: False)
    bag = []
    heapq.heappush(bag, (0, source, None))
    while len(bag) > 0:
        distance, current, parent = heapq.heappop(bag)
        if current == destination:
            seen[current] = parent
            return distance, seen
        if not seen[current]:
            seen[current] = parent
            neighbors = []
            for move in [(0,1), (0,-1), (1,0), (-1,0)]:
                v = (current[0] + move[0], current[1] + move[1])
                if graph[v] != "#":
                    neighbors.append(v)
            for neighbor in neighbors:
                heapq.heappush(
                    bag,
                    (1 + distance, neighbor, current),
                )
    return inf, seen

with open("2024/input/day18") as f:
    data = f.read().splitlines()

size = 71
grid = defaultdict(lambda: "#")
for i in range(size):
    for j in range(size):
        grid[i,j] = "."

for i in range(len(data)):
    d = 0
    x = int(data[i].split(",")[0])
    y = int(data[i].split(",")[1])
    p = (y,x)
    grid[p] = "#"
    if i >= 1023:
        d, s = dijkstra(grid, (0,0), (size-1, size-1))
    if i == 1023:
        print("Part 1:", d)
    if d == inf:
        print("Part 2:", f"{p[1]},{p[0]}")
        break
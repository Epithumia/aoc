from collections import defaultdict


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


cpu = defaultdict(lambda: "#")

with open("2024/input/day20", "r") as f:
    data = f.read().splitlines()

    for i in range(len(data)):
        for j in range(len(data[0])):
            cpu[i, j] = data[i][j]
            if data[i][j] == "S":
                start = (i, j)
            elif data[i][j] == "E":
                end = (i, j)


original_path = [start]
seen = set(start)
current = start
while current != end:
    neighbors = []
    for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        v = (current[0] + move[0], current[1] + move[1])
        if cpu[v] != "#" and v not in seen:
            original_path.append(v)
            seen.add(v)
            current = v
            break

part1 = 0
part2 = 0
cutoff = 99

for i in range(len(original_path) - (cutoff + 3)):
    for j in range(i + (cutoff + 3), len(original_path)):
        cheat = manhattan_distance(original_path[i], original_path[j])
        if 2 <= cheat <= 20 and j - i - cheat > cutoff:
            part2 += 1
            if cheat == 2:
                part1 += 1

print("Part 1:", part1)
print("Part 2:", part2)

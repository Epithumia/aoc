from collections import defaultdict
from functools import cmp_to_key

order = defaultdict(lambda: list())
part1 = 0
part2 = 0


def update_sort(a, b):
    if b in order[a]:
        return -1
    if a in order[b]:
        return 1
    return 0


with open("2024/input/day05") as f:
    data = f.read().splitlines()

    for line in data:
        if "|" in line:
            order[int(line.split("|")[0])].append(int(line.split("|")[1]))

        if "," in line:
            update = [int(x) for x in line.split(",")]
            u = sorted(update[:], key=cmp_to_key(update_sort))
            if str(u) == str(update):
                part1 += update[len(update) // 2]
            else:
                part2 += u[len(u) // 2]

print("Part 1:", part1)
print("Part 2:", part2)

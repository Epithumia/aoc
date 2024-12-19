from functools import cache


@cache
def all_options(target, towels):
    if len(target) == 0:
        return 1
    count = 0
    for t in towels:
        if t == target[: len(t)]:
            count += all_options(target[len(t) :], towels)
    return count


with open("2024/input/day19") as f:
    data = f.read().splitlines()
    towels = tuple(x for x in data[0].split(", "))
    targets = [x for x in data[2:]]

print("Part 1:", sum([1 if all_options(x, tuple(towels)) else 0 for x in targets]))

print("Part 2:", sum([all_options(x, tuple(towels)) for x in targets]))

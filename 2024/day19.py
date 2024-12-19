from functools import cache


def all_options(target, towels):

    @cache
    def find(target):
        if len(target) == 0:
            return 1
        count = 0
        for t in towels:
            if t == target[: len(t)]:
                count += find(target[len(t) :])
        return count

    return find(target)


with open("2024/input/day19") as f:
    data = f.read().splitlines()
    towels = data[0].split(", ")
    targets = [x for x in data[2:]]

options = [all_options(x, towels) for x in targets]

print("Part 1:", sum(1 for x in options if x > 0))

print("Part 2:", sum(options))

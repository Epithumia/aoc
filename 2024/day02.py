from typing import List

reports = []


def prepare(report: List[int]) -> List[int]:
    prepared = []
    increasing = report[0] < report[1]
    for i in range(0, len(report) - 1):
        if increasing:
            prepared.append(report[i + 1] - report[i])
        else:
            prepared.append(report[i] - report[i + 1])
    return prepared


def check(prepared: List[int]) -> bool:
    errors = 0
    for v in prepared:
        if not (0 < v < 4):
            errors += 1
    return errors


with open("2024/input/day02") as f:
    data = f.read().splitlines()

    for line in data:
        reports.append(prepare([int(x) for x in line.split(" ")]))

print("Part 1", sum([1 for x in reports if check(x) < 1]))
print("Part 2", sum([1 for x in reports if check(x) <= 1]))

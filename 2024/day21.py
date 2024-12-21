from functools import cache
import heapq
from math import inf

PAD = {
    "0": {"A": ">", "2": "^"},
    "1": {"4": "^", "2": ">"},
    "2": {"0": "v", "1": "<", "3": ">", "5": "^"},
    "3": {"A": "v", "2": "<", "6": "^"},
    "4": {"1": "v", "5": ">", "7": "^"},
    "5": {"2": "v", "4": "<", "6": ">", "8": "^"},
    "6": {"3": "v", "5": "<", "9": "^"},
    "7": {"4": "v", "8": ">"},
    "8": {"5": "v", "7": "<", "9": ">"},
    "9": {"6": "v", "8": "<"},
    "A": {"0": "<", "3": "^"},
}


@cache
def keypad(state, target, depth=0):
    if depth == 0:
        return 1  # target
    if state == target:
        return keypad("A", "A", depth - 1)
    if state == "A" and target == "^":
        return keypad("A", "<", depth - 1) + keypad("<", "A", depth - 1)
    if state == "A" and target == ">":
        return keypad("A", "v", depth - 1) + keypad("v", "A", depth - 1)
    if state == "A" and target == "v":
        a = (
            keypad("A", "<", depth - 1)
            + keypad("<", "v", depth - 1)
            + keypad("v", "A", depth - 1)
        )
        b = (
            keypad("A", "v", depth - 1)
            + keypad("v", "<", depth - 1)
            + keypad("<", "A", depth - 1)
        )
        if a <= b:  # if len(a) <= len(b):
            return a
        return b
    if state == "A" and target == "<":
        a = (
            keypad("A", "v", depth - 1)
            + keypad("v", "<", depth - 1)
            + keypad("<", "<", depth - 1)
            + keypad("<", "A", depth - 1)
        )
        b = (
            keypad("A", "<", depth - 1)
            + keypad("<", "v", depth - 1)
            + keypad("v", "<", depth - 1)
            + keypad("<", "A", depth - 1)
        )
        if a <= b:  # if len(a) <= len(b):
            return a
        return b

    if state == "^" and target == "A":
        return keypad("A", ">", depth - 1) + keypad(">", "A", depth - 1)
    if state == "^" and target == ">":
        a = (
            keypad("A", "v", depth - 1)
            + keypad("v", ">", depth - 1)
            + keypad(">", "A", depth - 1)
        )
        b = (
            keypad("A", ">", depth - 1)
            + keypad(">", "v", depth - 1)
            + keypad("v", "A", depth - 1)
        )
        if a <= b:  # if len(a) <= len(b):
            return a
        return b
    if state == "^" and target == "<":
        return (
            keypad("A", "v", depth - 1)
            + keypad("v", "<", depth - 1)
            + keypad("<", "A", depth - 1)
        )

    if state == ">" and target == "A":
        return keypad("A", "^", depth - 1) + keypad("^", "A", depth - 1)
    if state == ">" and target == "v":
        return keypad("A", "<", depth - 1) + keypad("<", "A", depth - 1)
    if state == ">" and target == "^":
        a = (
            keypad("A", "^", depth - 1)
            + keypad("^", "<", depth - 1)
            + keypad("<", "A", depth - 1)
        )
        b = (
            keypad("A", "<", depth - 1)
            + keypad("<", "^", depth - 1)
            + keypad("^", "A", depth - 1)
        )
        if a <= b:  # if len(a) <= len(b):
            return a
        return b

    if state == "v" and target == "A":
        a = (
            keypad("A", "^", depth - 1)
            + keypad("^", ">", depth - 1)
            + keypad(">", "A", depth - 1)
        )
        b = (
            keypad("A", ">", depth - 1)
            + keypad(">", "^", depth - 1)
            + keypad("^", "A", depth - 1)
        )
        if a <= b:  # if len(a) <= len(b):
            return a
        return b
    if state == "v" and target == ">":
        return keypad("A", ">", depth - 1) + keypad(">", "A", depth - 1)
    if state == "v" and target == "<":
        return keypad("A", "<", depth - 1) + keypad("<", "A", depth - 1)

    if state == "<" and target == "A":
        a = (
            keypad("A", ">", depth - 1)
            + keypad(">", ">", depth - 1)
            + keypad(">", "^", depth - 1)
            + keypad("^", "A", depth - 1)
        )
        b = (
            keypad("A", ">", depth - 1)
            + keypad(">", "^", depth - 1)
            + keypad("^", ">", depth - 1)
            + keypad(">", "A", depth - 1)
        )
        if a <= b:  # if len(a) <= len(b):
            return a
        return b
    if state == "<" and target == "^":
        return (
            keypad("A", ">", depth - 1)
            + keypad(">", "^", depth - 1)
            + keypad("^", "A", depth - 1)
        )
    if state == "<" and target == "v":
        return keypad("A", ">", depth - 1) + keypad(">", "A", depth - 1)


def digipad(state, target, depth=2):
    queue = []
    seen = set()
    heapq.heappush(queue, (0, state))
    while len(queue) > 0:
        (cost, sequence) = heapq.heappop(queue)
        if len(sequence) > 1 and sequence[-1] == target:
            return cost
        if sequence in seen:
            continue
        seen.add(sequence)
        for m in PAD[sequence[-1]]:
            if m not in sequence:
                mc = sequence[:] + m
                cost = 0
                first = keypad("A", PAD[mc[0]][mc[1]], depth)
                last = keypad(PAD[mc[-2]][mc[-1]], "A", depth)
                for k in range(1, len(mc) - 1):
                    cost += keypad(PAD[mc[k - 1]][mc[k]], PAD[mc[k]][mc[k + 1]], depth)
                cost += first + last
                heapq.heappush(queue, (cost, mc))

    return inf


with open("2024/input/day21") as f:
    data = f.read().splitlines()

k1 = 2
k2 = 25

part1 = 0
part2 = 0
for row in data:
    current = "A"
    cost1 = 0
    cost2 = 0
    for c in row:
        cost1 += digipad(current, c, k1)
        cost2 += digipad(current, c, k2)
        current = c
    num = int(row.replace("A", ""))
    part1 += cost1 * num
    part2 += cost2 * num

print("Part 1:", part1)
print("Part 2:", part2)

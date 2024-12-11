from functools import cache

with open("2024/input/day11") as f:
    stones = [int(x) for x in f.read().split(" ")]


@cache
def blink(stone, times):
    if times == 0:
        return 1
    if stone == 0:
        return blink(1, times - 1)
    if len(str(stone)) % 2 == 0:
        s = str(stone)
        s1 = s[: len(s) // 2]
        s2 = s[len(s) // 2 :]
        return blink(int(s1), times - 1) + blink(int(s2), times - 1)
    return blink(stone * 2024, times - 1)


print("Part 1:", sum([blink(stone, 25) for stone in stones]))
print("Part 2:", sum([blink(stone, 75) for stone in stones]))

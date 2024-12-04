from collections import defaultdict

mapping = defaultdict(lambda: ".")

with open("2024/input/day04") as f:
    data = f.read().splitlines()

    for i in range(len(data)):
        for j in range(len(data[0])):
            mapping[i, j] = data[i][j]

xmas_count = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if mapping[i, j] == "X":
            # right
            if (
                mapping[i, j + 1] == "M"
                and mapping[i, j + 2] == "A"
                and mapping[i, j + 3] == "S"
            ):
                xmas_count += 1
            # down
            if (
                mapping[i + 1, j] == "M"
                and mapping[i + 2, j] == "A"
                and mapping[i + 3, j] == "S"
            ):
                xmas_count += 1
            # left
            if (
                mapping[i, j - 1] == "M"
                and mapping[i, j - 2] == "A"
                and mapping[i, j - 3] == "S"
            ):
                xmas_count += 1
            # up
            if (
                mapping[i - 1, j] == "M"
                and mapping[i - 2, j] == "A"
                and mapping[i - 3, j] == "S"
            ):
                xmas_count += 1
            # left down
            if (
                mapping[i + 1, j - 1] == "M"
                and mapping[i + 2, j - 2] == "A"
                and mapping[i + 3, j - 3] == "S"
            ):
                xmas_count += 1
            # right down
            if (
                mapping[i + 1, j + 1] == "M"
                and mapping[i + 2, j + 2] == "A"
                and mapping[i + 3, j + 3] == "S"
            ):
                xmas_count += 1
            # left up
            if (
                mapping[i - 1, j - 1] == "M"
                and mapping[i - 2, j - 2] == "A"
                and mapping[i - 3, j - 3] == "S"
            ):
                xmas_count += 1
            # right up
            if (
                mapping[i - 1, j + 1] == "M"
                and mapping[i - 2, j + 2] == "A"
                and mapping[i - 3, j + 3] == "S"
            ):
                xmas_count += 1

print("Part 1:", xmas_count)

mas_count = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if mapping[i, j] == "A":
            if (
                mapping[i - 1, j - 1] == "M"
                and mapping[i - 1, j + 1] == "M"
                and mapping[i + 1, j - 1] == "S"
                and mapping[i + 1, j + 1] == "S"
            ):
                mas_count += 1
            if (
                mapping[i - 1, j - 1] == "M"
                and mapping[i - 1, j + 1] == "S"
                and mapping[i + 1, j - 1] == "M"
                and mapping[i + 1, j + 1] == "S"
            ):
                mas_count += 1
            if (
                mapping[i - 1, j - 1] == "S"
                and mapping[i - 1, j + 1] == "S"
                and mapping[i + 1, j - 1] == "M"
                and mapping[i + 1, j + 1] == "M"
            ):
                mas_count += 1
            if (
                mapping[i - 1, j - 1] == "S"
                and mapping[i - 1, j + 1] == "M"
                and mapping[i + 1, j - 1] == "S"
                and mapping[i + 1, j + 1] == "M"
            ):
                mas_count += 1

print("Part 2:", mas_count)

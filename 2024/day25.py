keys = []
locks = []

with open("2024/input/day25") as f:
    data = f.read().splitlines()

    for i in range((len(data) + 1) // 8):
        item = tuple()
        for c in range(5):
            item += (
                sum([1 if data[8 * i + r][c] == "#" else 0 for r in range(7)]) - 1,
            )
        if data[8 * i][0] == "#":
            keys.append(item)
        else:
            locks.append(item)

print(
    "Part 1:",
    sum(
        [
            1 if all([key[i] + lock[i] < 6 for i in range(5)]) else 0
            for key in keys
            for lock in locks
        ]
    ),
)

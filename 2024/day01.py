left = []
right = []

with open("2024/input/day01") as f:
    data = f.read().splitlines()

    for line in data:
        d = line.split(" ")
        left.append(int(d[0]))
        right.append(int(d[-1]))

left = sorted(left)
right = sorted(right)

dist = 0
similarity = 0

for i in range(len(left)):
    dist += abs(left[i] - right[i])
    n = sum(1 for x in right if x == left[i])
    similarity += n * left[i]

print("Part 1:", dist)
print("Part 2:", similarity)

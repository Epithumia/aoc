dial = 50
count = 0
count2 = 0

with open("2025/input/day01") as f:
    data = f.read().splitlines()

    for line in data:
        d = line[0]
        v = int(line[1:])

        if d == "R":
            if dial + v > 100:
                count2 += (dial + v) // 100
                if (dial + v) % 100 == 0:
                    count2 -= 1
            dial = (dial + v) % 100
        else:
            if dial - v < 0:
                count2 += abs(dial - v) // 100 + 1
                if (dial - v) % 100 == 0 or dial == 0:
                    count2 -= 1
            dial = (dial - v) % 100

        if dial == 0:
            count += 1

print(f"Part 1 : {count}")
print(f"Part 2 : {count2+count}")
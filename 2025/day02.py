def gen_repeat(i):
    match i:
        case 2:
            for j in range(10):
                yield int(f"{j}{j}")
        case 3:
            for j in range(10):
                yield int(f"{j}{j}{j}")
        case 4:
            for j in range(10):
                yield int(f"{j}{j}{j}{j}")
            for j in range(10, 100):
                yield int(f"{j}{j}")
        case 5:
            for j in range(10):
                yield int(f"{j}{j}{j}{j}{j}")
        case 6:
            for j in range(10, 100):
                yield int(f"{j}{j}{j}")
            for j in range(100, 1000):
                yield int(f"{j}{j}")
        case 7:
            for j in range(10):
                yield int(f"{j}{j}{j}{j}{j}{j}{j}")
        case 8:
            for j in range(1000, 10000):
                yield int(f"{j}{j}")
        case 9:
            for j in range(100, 1000):
                yield int(f"{j}{j}{j}")
        case 10:
            for j in range(10, 100):
                yield int(f"{j}{j}{j}{j}{j}")
            for j in range(10000, 100000):
                yield int(f"{j}{j}")


with open("2025/input/day02") as f:
    data = f.read().splitlines()[0]
    raw_ranges = data.split(",")
    ranges = [x.split("-") for x in raw_ranges]

score1 = 0
score2 = 0

for r in ranges:
    if len(r[0]) % 2 == 0 or len(r[1]) % 2 == 0 or (len(r[1]) - len(r[0])) >= 2:
        if len(r[0]) % 2:
            start = r[0].rjust(len(r[0]) + 1, "0")
        else:
            start = r[0]
        if len(r[1]) % 2:
            end = r[1].ljust(len(r[1]) + 1, "0")
        else:
            end = r[1]
        start = int(start[0 : len(start) // 2])
        end = int(end[0 : len(end) // 2])

        for i in range(start, end + 1):
            val = int(f"{i}{i}")
            if int(r[0]) <= val <= int(r[1]):
                score1 += val

print(f"Partie 1: {score1}")

for r in ranges:
    for size in range(len(r[0]), len(r[1]) + 1):
        seen = set()
        for val in gen_repeat(size):
            if val not in seen and int(r[0]) <= val <= int(r[1]):
                seen.add(val)
                score2 += val

print(f"Partie 2: {score2}")

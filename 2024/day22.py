from collections import defaultdict
from tqdm import tqdm


def generate(number, rounds):
    for _ in range(rounds):
        number = (number ^ (number << 6)) & (2**24 - 1)
        number = (number ^ (number >> 5)) & (2**24 - 1)
        number = (number ^ (number << 11)) & (2**24 - 1)
    return number


def gen_prices(seed):
    number = seed
    number = (number ^ (number << 6)) & (2**24 - 1)
    number = (number ^ (number >> 5)) & (2**24 - 1)
    number = (number ^ (number << 11)) & (2**24 - 1)
    i = 0
    while i < 2000:
        yield number
        i += 1
        number = (number ^ (number << 6)) & (2**24 - 1)
        number = (number ^ (number >> 5)) & (2**24 - 1)
        number = (number ^ (number << 11)) & (2**24 - 1)


with open("2024/input/day22") as f:
    data = f.read().splitlines()
    seeds = [int(x) for x in data]

part1 = sum([generate(seed, 2000) for seed in seeds])
print("Part 1:", part1)

sequences = defaultdict(lambda: 0)

for seed in tqdm(seeds):
    pa = seed % 10
    d = []
    i = 0
    for v in gen_prices(seed):
        pb = v % 10
        d.append(pb - pa)
        pa = pb
        if i > 3:
            sequence = str(d[-4:])
            if (seed, sequence) not in sequences:
                sequences[seed, sequence] = pa
        i += 1

reference = list(k[1] for k in sequences.keys() if k[0] == seeds[0])

best = 0
for sequence in tqdm(reference):
    best = max(best, sum([sequences[(seed, sequence)] for seed in seeds]))

print("Part 2:", best)

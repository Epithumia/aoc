import re

with open("2024/input/day03") as f:
    data = f.read().splitlines()
    data = "".join(data)  # F you, carriage return


mul = re.findall(r"mul\((\d+?),(\d+?)\)", data)
res1 = sum([int(x[0]) * int(x[1]) for x in mul])

print("Part 1:", res1)

dos = re.sub("don't\(\).*?do\(\)", "", data)
mul = re.findall(r"mul\((\d+?),(\d+?)\)", dos)
res2 = sum([int(x[0]) * int(x[1]) for x in mul])

print("Part 2:", res2)

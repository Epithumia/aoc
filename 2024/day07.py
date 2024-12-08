equations = []

with open("2024/input/day07") as f:
    data = f.read().splitlines()

    for line in data:
        left, right = line.split(": ")
        left = int(left)
        right = [int(x) for x in right.split(" ")]
        eq = [left]
        eq.extend(right)
        equations.append(eq)


def solve(target, values, super=False):
    if len(values) == 1 and target == values[-1]:
        return True
    if len(values) == 0 or target < 0 or (target == 0 and len(values) > 0):
        return False
    divisible = False
    if target % values[-1] == 0:
        divisible = solve(target // values[-1], values[:-1], super)
    if divisible:
        return True
    if super:
        concatenate = False
        concat_l = str(target)
        concat_r = str(values[-1])
        if concat_l.endswith(concat_r):
            concat_l = concat_l[: -len(concat_r)]
            if concat_l == "":
                concat_l = "-1"
            concatenate = solve(int(concat_l), values[:-1], super)
        if concatenate:
            return True
    target = target - values[-1]
    return solve(target, values[:-1], super)


calibration = 0
for eq in equations:
    target = eq[0]
    values = eq[1:]
    res = solve(target, values)
    if res:
        calibration += target

print("Part 1:", calibration)

calibration = 0
for eq in equations:
    target = eq[0]
    values = eq[1:]
    res = solve(target, values, True)
    if res:
        calibration += target

print("Part 2:", calibration)

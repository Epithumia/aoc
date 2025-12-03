partie1 = 0
partie2 = 0
data = []

with open("2025/input/day03") as f:
    input = f.read().splitlines()

    for line in input:
        data.append([int(x) for x in line])

for row in data:
    x = row.index(max(row[0:-1]))
    a = row[x]
    b = max(row[x + 1 :])

    partie1 += 10*a+b

print("Partie 1:", partie1)

for row in data:
    n = 0
    x = 0
    window = row[:]
    for i in range(12):
        p = 11 - i
        
        if p > 0:
            v = max(window[0:-p])
            n += (10**p) * v
            x = window.index(v) + 1
            window = window[x:]
        else:
            v = max(window)
            n += (10**p) * v
    partie2 += n
        

print("Partie 2:", partie2)
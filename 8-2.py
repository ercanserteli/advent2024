from collections import defaultdict
from math import gcd


def simplify_pair(a, b):
    cd = gcd(a, b)
    return (a // cd, b // cd)


inp = []
with open("8-input.txt") as f:
    for line in f:
        inp.append(line[:-1])

height = len(inp)
width = len(inp[0])
antenna_map = defaultdict(list)
for y, row in enumerate(inp):
    for x, cell in enumerate(row):
        if cell != ".":
            antenna_map[cell].append((x, y))

antinodes = set()
for freq, positions in antenna_map.items():
    for i, (x1, y1) in enumerate(positions):
        for j, (x2, y2) in enumerate(positions):
            if i == j:
                continue

            dx, dy = simplify_pair(x2 - x1, y2 - y1)

            ax = x1
            ay = y1
            while True:
                ax -= dx
                ay -= dy
                if ax >= 0 and ay >= 0 and ax < width and ay < height:
                    antinodes.add((ax, ay))
                else:
                    break

            ax = x1
            ay = y1
            while True:
                ax += dx
                ay += dy
                if ax >= 0 and ay >= 0 and ax < width and ay < height:
                    antinodes.add((ax, ay))
                else:
                    break

print(len(antinodes))

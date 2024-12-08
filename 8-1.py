from collections import defaultdict

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
            dx = x2 - x1
            dy = y2 - y1

            ax1 = x1 - dx
            ay1 = y1 - dy
            ax2 = x2 + dx
            ay2 = y2 + dy

            if ax1 >= 0 and ay1 >= 0 and ax1 < width and ay1 < height:
                antinodes.add((ax1, ay1))
            if ax2 >= 0 and ay2 >= 0 and ax2 < width and ay2 < height:
                antinodes.add((ax2, ay2))

print(len(antinodes))

inp = []
with open("4-input.txt") as f:
    for line in f:
        inp.append(line[:-1])

count = 0
height = len(inp)
width = len(inp[0])
for y, row in enumerate(inp):
    for x, c in enumerate(row):
        if c == "X":
            # Check right
            if x < width - 3 and row[x + 1 : x + 4] == "MAS":
                count += 1
            # Check down
            if (
                y < height - 3
                and inp[y + 1][x] == "M"
                and inp[y + 2][x] == "A"
                and inp[y + 3][x] == "S"
            ):
                count += 1
            # Check left
            if x >= 3 and row[x - 3 : x] == "SAM":
                count += 1
            # Check up
            if (
                y >= 3
                and inp[y - 1][x] == "M"
                and inp[y - 2][x] == "A"
                and inp[y - 3][x] == "S"
            ):
                count += 1
            # Check down-right
            if (
                x < width - 3
                and y < height - 3
                and inp[y + 1][x + 1] == "M"
                and inp[y + 2][x + 2] == "A"
                and inp[y + 3][x + 3] == "S"
            ):
                count += 1
            # Check down-left
            if (
                x >= 3
                and y < height - 3
                and inp[y + 1][x - 1] == "M"
                and inp[y + 2][x - 2] == "A"
                and inp[y + 3][x - 3] == "S"
            ):
                count += 1
            # Check up-right
            if (
                x < width - 3
                and y >= 3
                and inp[y - 1][x + 1] == "M"
                and inp[y - 2][x + 2] == "A"
                and inp[y - 3][x + 3] == "S"
            ):
                count += 1
            # Check up-left
            if (
                x >= 3
                and y >= 3
                and inp[y - 1][x - 1] == "M"
                and inp[y - 2][x - 2] == "A"
                and inp[y - 3][x - 3] == "S"
            ):
                count += 1

print(count)

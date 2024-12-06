inp = []
with open("4-input.txt") as f:
    for line in f:
        inp.append(line[:-1])

count = 0
height = len(inp)
width = len(inp[0])
for y, row in list(enumerate(inp))[1:-1]:
    for x, c in list(enumerate(row))[1:-1]:
        if c == "A":
            top_left = inp[y - 1][x - 1]
            top_right = inp[y - 1][x + 1]
            bot_left = inp[y + 1][x - 1]
            bot_right = inp[y + 1][x + 1]

            if (
                (top_left == "S" and bot_right == "M")
                or (top_left == "M" and bot_right == "S")
            ) and (
                (top_right == "S" and bot_left == "M")
                or (top_right == "M" and bot_left == "S")
            ):
                count += 1

print(count)

a = []
b = []
with open("1-input.txt") as f:
    for line in f:
        nums = line.split()
        a.append(int(nums[0]))
        b.append(int(nums[1]))

a.sort()
b.sort()

diff = 0
for x, y in zip(a, b):
    diff += abs(x - y)

print(diff)

similarity = 0
for x in a:
    x_count = 0
    for y in b:
        if y > x:
            break
        if y == x:
            x_count += x

    similarity += x_count

print(similarity)

inp = []
with open("7-input.txt") as f:
    for line in f:
        value, operands = line[:-1].split(": ")
        operands = operands.split()
        inp.append((int(value), list(map(int, operands))))


def search(ops):
    if len(ops) == 1:
        return [ops[0]]

    a = [ops[0] + ops[1]]
    b = [ops[0] * ops[1]]
    c = [int(f"{ops[0]}{ops[1]}")]
    if len(ops) > 2:
        a.extend(ops[2:])
        b.extend(ops[2:])
        c.extend(ops[2:])
    return search(a) + search(b) + search(c)


result = 0
for value, operands in inp:
    if value in search(operands):
        result += value

print(result)

inp = []
with open("2-input.txt") as f:
    inp.append(map(f.readline().split(), lambda s: int(s)))

safe_count = 0
for report in inp:
    first_diff = report[1] - report[0]
    if first_diff == 0 or abs(first_diff) > 3:
        continue
    is_safe = True
    diff_sign = first_diff / abs(first_diff)
    for i, level in list(enumerate(report))[2:]:
        diff = diff_sign * (level - report[i - 1])
        if diff <= 0 or diff > 3:
            is_safe = False
            break
    if is_safe:
        safe_count += 1

print(safe_count)

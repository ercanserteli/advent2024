inp = []
with open("2-input.txt") as f:
    for line in f:
        inp.append(list(map(lambda s: int(s), line.split())))


def check_safety(rep):
    first_diff = rep[1] - rep[0]
    if first_diff == 0 or abs(first_diff) > 3:
        return 0

    diff_sign = first_diff / abs(first_diff)
    for i, level in list(enumerate(rep))[2:]:
        diff = diff_sign * (level - rep[i - 1])
        if diff <= 0 or diff > 3:
            return i - 1

    return -1


safe_count = 0
for report in inp:
    is_safe = True
    bad_level = check_safety(report)
    if bad_level >= 0:
        report_1 = report[:bad_level] + report[bad_level + 1 :]
        if check_safety(report_1) >= 0:
            report_2 = report[: bad_level + 1] + report[bad_level + 2 :]
            if check_safety(report_2) >= 0:
                report_3 = report[: bad_level - 1] + report[bad_level:]
                if check_safety(report_3) >= 0:
                    is_safe = False

    if is_safe:
        safe_count += 1

print(safe_count)

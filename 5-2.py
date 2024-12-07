from collections import defaultdict

rules = []
updates = []

with open("5-input.txt") as f:
    # Load rules
    for line in f:
        if len(line) == 1:
            break
        rules.append(list(map(int, line[:-1].split("|"))))

    # Load updates
    for line in f:
        updates.append(list(map(int, line[:-1].split(","))))

rule_map = defaultdict(list)
for low, high in rules:
    rule_map[low].append(high)

result = 0
for update in updates:
    index_map = {}
    is_ordered = True
    for i, page in enumerate(update):
        index_map[page] = i
        page_rules = rule_map[page]
        for high in page_rules:
            if high in index_map:
                is_ordered = False
                break

        if not is_ordered:
            break

    if not is_ordered:
        old_update = update[:]
        print(update, "is not ordererd")
        while not is_ordered:
            new_index_map = {}
            is_ordered = True
            for i, page in enumerate(update):
                new_index_map[page] = i
                page_rules = rule_map[page]
                for high in page_rules:
                    high_index = new_index_map.get(high)
                    if high_index is not None:
                        update.pop(i)
                        update.insert(high_index, page)
                        is_ordered = False
                        break
                if not is_ordered:
                    break

        print(update, "is now ordererd\n")
        result += update[int(len(update) / 2)]

print(result)

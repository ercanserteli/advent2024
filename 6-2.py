class Dir:
    def __init__(self, offset, next_dir):
        self.offset = offset
        self.next_dir = next_dir


left = Dir((-1, 0), None)
down = Dir((0, 1), left)
right = Dir((1, 0), down)
up = Dir((0, -1), right)
left.next_dir = up


def get_next_pos():
    offset = guard_dir.offset
    next_pos = (guard_pos[0] + offset[0], guard_pos[1] + offset[1])
    next_tile = None
    if not is_out_of_bounds(next_pos):
        next_tile = room[next_pos[1]][next_pos[0]]
    return next_pos, next_tile


# Returns whether it started to loop
def move(obstacle_encounters=None):
    global guard_pos
    global guard_dir

    while True:
        next_pos, next_tile = get_next_pos()
        if next_tile == "#":
            # Obstacle ahead
            if obstacle_encounters is not None:
                encounter = (guard_pos, next_pos)
                if encounter in obstacle_encounters:
                    return True
                obstacle_encounters.add(encounter)

            guard_dir = guard_dir.next_dir
            next_pos, next_tile = get_next_pos()
        else:
            break
    guard_pos = next_pos
    return False


def is_out_of_bounds(pos):
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= width or pos[1] >= height


room = []
guard_pos = None
org_guard_pos = None
with open("6-input.txt") as f:
    for y, line in enumerate(f):
        row = line[:-1]
        room.append(row)
        if guard_pos is None:
            try:
                x = row.index("^")
                org_guard_pos = guard_pos = (x, y)
                print("Guard pos:", guard_pos)
            except ValueError:
                pass

height = len(room)
width = len(room[0])
guard_dir = up

distinct_path = set()
while True:
    distinct_path.add(guard_pos)
    move()
    if is_out_of_bounds(guard_pos):
        break

result = 0
for y in range(height):
    org_row = room[y]
    for x in range(width):
        if org_row[x] != "." or (x, y) not in distinct_path:
            continue

        guard_pos = org_guard_pos
        guard_dir = up
        obstacle_encounters = set()
        room[y] = org_row[:x] + "#" + org_row[x + 1:]
        while True:
            did_loop = move(obstacle_encounters)
            if did_loop:
                result += 1
                break
            if is_out_of_bounds(guard_pos):
                break

    room[y] = org_row

print(result)

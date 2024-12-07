from enum import Enum


class Dir(Enum):
    up = 1
    right = 2
    down = 3
    left = 4


dir_offsets = {Dir.up: (0, -1), Dir.right: (1, 0), Dir.down: (0, 1), Dir.left: (-1, 0)}
dir_rotates = {
    Dir.up: Dir.right,
    Dir.right: Dir.down,
    Dir.down: Dir.left,
    Dir.left: Dir.up,
}


def get_next_pos():
    offset = dir_offsets[guard_dir]
    next_pos = (guard_pos[0] + offset[0], guard_pos[1] + offset[1])
    return next_pos, room[next_pos[1]][next_pos[0]]


def move():
    global guard_pos
    global guard_dir

    while True:
        next_pos, next_tile = get_next_pos()
        if next_tile == "#":
            # Obstacle ahead
            guard_dir = dir_rotates[guard_dir]
            next_pos, next_tile = get_next_pos()
        else:
            break
    guard_pos = next_pos


room = []
guard_pos = None
with open("6-input.txt") as f:
    for y, line in enumerate(f):
        row = line[:-1]
        room.append(row)
        if guard_pos is None:
            try:
                x = row.index("^")
                guard_pos = (x, y)
                print("Guard pos:", guard_pos)
            except ValueError:
                pass

height = len(room)
width = len(room[0])
guard_dir = Dir.up
distinct_path = set()
while True:
    distinct_path.add(guard_pos)
    move()
    if (
        guard_pos[0] < 0
        or guard_pos[1] < 0
        or guard_pos[0] >= width
        or guard_pos[1] >= height
    ):
        break

print(len(distinct_path))

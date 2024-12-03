from enum import Enum

inp = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
with open("3-input.txt") as f:
    inp = f.read()


class State(Enum):
    begin = 1
    number_one = 2
    comma = 3
    number_two = 4
    end = 5


def get_number(s):
    for i in range(3, 0, -1):
        try:
            # print(f"Trying {s}")
            return int(s[:i]), i
        except ValueError:
            pass
    return None, None


beginning = "mul("
middle = ","
end = ")"

i = 0
n1 = 0
n2 = 0
result = 0
state = State.begin
while i < len(inp):
    if state == State.begin:
        if len(inp) > i + 4 and inp[i : i + 4] == "mul(":
            print(f"Found {state.name} at {i}")
            state = State.number_one
            i += 4
        else:
            i += 1

    elif state == State.number_one:
        n1, digits = get_number(inp[i : i + 3])
        if n1 is not None:
            print(f"Found {state.name} at {i}")
            i += digits
            state = State.comma
        else:
            state = State.begin

    elif state == State.comma:
        if inp[i] == ",":
            print(f"Found {state.name} at {i}")
            i += 1
            state = State.number_two
        else:
            state = State.begin

    elif state == State.number_two:
        n2, digits = get_number(inp[i : i + 3])
        if n2 is not None:
            print(f"Found {state.name} at {i}")
            i += digits
            state = State.end
        else:
            state = State.begin

    elif state == State.end:
        if inp[i] == ")":
            print(f"Found {state.name} at {i}")
            result += n1 * n2
            i += 1
        state = State.begin

print(result)

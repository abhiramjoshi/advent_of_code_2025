import sys

INPUT_FILE = sys.argv[1]

machines = []
with open(INPUT_FILE, "r") as f:
    machines = [line.rstrip("\n") for line in f.readlines()]


def recurse(
    i: int,
    sequence: int,
    presses: int,
    min_presses: int,
    buttons: list[int],
    target: int,
):
    if sequence == target:
        min_presses = min(presses, min_presses)

    if i >= len(buttons):
        return min_presses

    take = recurse(
        i + 1, buttons[i] ^ sequence, presses + 1, min_presses, buttons, target
    )
    skip = recurse(i + 1, sequence, presses, min_presses, buttons, target)

    return min(skip, take)


total_presses = 0
for machine in machines:
    elements = machine.split(" ")
    seq = elements[0]
    buttons = elements[1:-1]

    sequence = 0
    for b in seq[1:-1]:
        sequence <<= 1
        if b == "#":
            sequence += 1

    # print(sequence)
    m = len(seq) - 2
    n = len(buttons)
    buttons_int = [0] * n
    for i in range(n):
        button = map(int, buttons[i][1:-1].split(","))
        button_bin = ["0"] * m
        for b in button:
            button_bin[b] = "1"

        buttons_int[i] = int("".join(button_bin), 2)
    # print(buttons)
    # print(buttons_int)

    presses = recurse(0, 0, 0, 10**9, buttons_int, sequence)

    print("Round presses:", presses)
    total_presses += presses

print("Total presses req:", total_presses)

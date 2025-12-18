# recursion is too slow, maybe use backtracking
import sys
from functools import cache

INPUT_FILE = sys.argv[1]

machines = []
with open(INPUT_FILE, "r") as f:
    machines = [line.rstrip("\n") for line in f.readlines()]


def check_matching_sequence(sequence):
    n = len(sequence)
    for i in range(n):
        if sequence[i] != TARGET[i]:
            return False

    return True


def check_invalid_sequence(sequence):
    n = len(sequence)
    for i in range(n):
        if sequence[i] > TARGET[i]:
            return True
    return False


@cache
def recurse(
    sequence: tuple[int],
    k: int,
):
    if check_matching_sequence(sequence):
        return 0

    if check_invalid_sequence(sequence):
        return float("inf")

    min_presses = float("inf")
    for i in range(k, len(BUTTONS)):
        new_seq = tuple([BUTTONS[i][j] + sequence[j] for j in range(len(sequence))])

        min_presses = min(recurse(new_seq, i) + 1, min_presses)
    return min_presses


total_presses = 0
for machine in machines:
    elements = machine.split(" ")
    seq = list(map(int, elements[-1].strip("{}").split(",")))
    buttons = elements[1:-1]
    print(seq)

    m = len(seq)
    n = len(buttons)
    buttons_int = [[0] * m] * n
    for i in range(n):
        button = map(int, buttons[i][1:-1].split(","))
        button_bin = [0] * m
        for b in button:
            button_bin[b] = 1

        buttons_int[i] = button_bin
    # print(buttons)
    print(buttons_int)
    BUTTONS = buttons_int
    TARGET = seq
    print("Using constants:")
    print(BUTTONS, TARGET)
    presses = recurse(tuple([0] * m), 0)

    print("Round presses:", presses)
    total_presses += presses

print("Total presses req:", total_presses)

# recursion is too slow, maybe use backtracking
import sys

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


def backtrack(presses: int, k: int):
    global MIN_PRESSES
    if presses > MIN_PRESSES:
        return

    if check_matching_sequence(SEQUENCE):
        MIN_PRESSES = min(MIN_PRESSES, presses)

    if check_invalid_sequence(SEQUENCE):
        return

    for i in range(k, len(BUTTONS)):
        for j in range(len(SEQUENCE)):
            SEQUENCE[j] += BUTTONS[i][j]
        backtrack(presses + 1, i)
        for j in range(len(SEQUENCE)):
            SEQUENCE[j] -= BUTTONS[i][j]


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
    MIN_PRESSES = float("inf")
    SEQUENCE = [0] * m
    print("Using constants:")
    print(BUTTONS, TARGET)
    presses = backtrack(0, 0)

    print("Round presses:", MIN_PRESSES)
    total_presses += MIN_PRESSES

print("Total presses req:", total_presses)

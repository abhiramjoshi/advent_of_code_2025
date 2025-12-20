import sys
from scipy.optimize import milp, LinearConstraint
import numpy as np


# Use linear programming
INPUT_FILE = sys.argv[1]

machines = []
with open(INPUT_FILE, "r") as f:
    machines = [line.rstrip("\n") for line in f.readlines()]


total_presses = 0
for machine in machines:
    elements = machine.split(" ")
    b = np.array(list(map(int, elements[-1].strip("{}").split(","))))
    buttons = elements[1:-1]
    m = b.shape[0]
    n = len(buttons)
    buttons_int = [[0] * m] * n
    for i in range(n):
        button = map(int, buttons[i][1:-1].split(","))
        button_bin = [0] * m
        for bit in button:
            button_bin[bit] = 1

        buttons_int[i] = button_bin
    A = np.array(buttons_int).transpose()
    print("A:", A)
    print("b:", b)
    b_m = np.full_like(b, np.inf, dtype=float)
    c = np.ones(A.shape[1])

    print("c:", c)
    constraints = LinearConstraint(A, b, b)
    integrality = np.ones_like(c)
    res = milp(c, integrality=integrality, constraints=constraints)
    press = np.sum(res.x)
    print("Presses:", res.x, press)
    total_presses += press

print("Total presses:", total_presses)

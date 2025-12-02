import sys

INPUT_FILE = sys.argv[1]
try:
    START = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    if START < 0 or START > 99:
        raise ValueError
except ValueError:
    print("Invalid start position")
    exit(1)

if not INPUT_FILE:
    exit(1)

rotations = []
with open(INPUT_FILE, "r") as file:
    rotations = file.readlines()

start = START
password = 0
for rotation in rotations:
    direction = rotation[0]
    dist = int(rotation[1:])

    if direction == "R":
        start += dist
    else:
        start -= dist

    start %= 100
    if start == 0:
        password += 1

print("The password is:", password)

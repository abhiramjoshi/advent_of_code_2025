import sys
from pprint import pprint
from collections import deque
from functools import cache

INPUT_FILE = sys.argv[1]

grid = []
with open(INPUT_FILE, "r") as f:
    for line in f.readlines():
        line = line.strip()
        grid.append([x for x in line])

n = len(grid)
m = len(grid[0])


@cache
def recurse(node: tuple[int, int]) -> int:
    x, y = node
    if y < 0 or y >= m:
        return 0

    if x == n:
        return 1

    ways = 0
    if grid[x][y] == "^":
        # left beam
        ways += recurse((x, y - 1))
        # right beam
        ways += recurse((x, y + 1))

    else:
        # go straight
        ways += recurse((x + 1, y))

    return ways


start = (0, 0)
for i in range(m):
    if grid[0][i] == "S":
        start = (0, i)
        break

s = recurse((start))
print("Number of timelines:", s)

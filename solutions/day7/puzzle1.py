import sys
from pprint import pprint
from collections import deque

INPUT_FILE = sys.argv[1]

grid = []
with open(INPUT_FILE, "r") as f:
    for line in f.readlines():
        line = line.strip()
        grid.append([x for x in line])

n = len(grid)
m = len(grid[0])


start = (0, 0)
for i in range(m):
    if grid[0][i] == "S":
        start = (0, i)
        break

splits = 0
queue = deque([start])
seen = set()
while queue:
    node = queue.popleft()
    x, y = node
    if node in seen:
        continue

    seen.add(node)

    if x == n:
        continue

    if grid[x][y] == "^":
        splits += 1
        for dy in [-1, 1]:
            if y + dy < 0 or y + dy >= m:
                continue
            if (x, y + dy) in seen:
                continue
            queue.append((x, y + dy))
    else:
        queue.append((x + 1, y))

print("Number of splits:", splits)

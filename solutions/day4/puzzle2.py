import sys

INPUT_FILE = sys.argv[1]

grid = []
with open(INPUT_FILE, "r") as f:
    for row in f.readlines():
        row.rstrip("\n")
        grid.append([i for i in row])

if not grid:
    print("Error processing grid")
    exit(1)


NEIGHBOURS = [
    (i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)
]

n = len(grid)
m = len(grid[0])


def check_neighbours(x: int, y: int, k: int) -> bool:
    t = 0
    for dx, dy in NEIGHBOURS:
        if x + dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= m:
            continue
        if grid[x+dx][y+dy] in ["@", "x"]:
            t += 1

        if t >= k:
            return False

    return True

prev_total = -1
total = 0
while total != prev_total:
    prev_total = total
    for i in range(n):
        for j in range(m):
            if grid[i][j] != "@":
                continue
            if check_neighbours(i, j, 4):
                # print(f"{(i,j)} can be removed")
                grid[i][j] = "x"
                total += 1
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "x":
                grid[i][j] = "."
    print("Total after run:", total)
print("Total rolls that can be removed:", total)

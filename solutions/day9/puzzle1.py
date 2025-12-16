# Find the largest rectangle, brute force it
import sys

INPUT_FILE = sys.argv[1]

tiles = []
with open(INPUT_FILE, "r") as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        tiles.append(list(map(int, line.split(","))))

# Brute force
largest = 0
n = len(tiles)
for i in range(n - 1):
    for j in range(1, n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        largest = max(largest, area)

print("The largest rectangle has an area of:", largest)

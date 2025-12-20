import sys

INPUT_FILE = sys.argv[1]

ranges = []
items = []

with open(INPUT_FILE, "r") as f:
    dest = True
    for line in f.readlines():
        line = line.rstrip("\n")
        if not line:
            dest = False
            continue

        if dest:
            ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))
        else:
            items.append(int(line))


items.sort()
ranges.sort(key=lambda x: x[0])

# Merge intervals
merged_intervals = []
m = len(ranges)

prev_start = ranges[0][0]
prev_end = ranges[0][1]
for i in range(1, m):
    start, end = ranges[i]
    if start > prev_end:
        merged_intervals.append((prev_start, prev_end))
        prev_start = start

    prev_end = max(end, prev_end)

merged_intervals.append((prev_start, prev_end))

n = len(merged_intervals)
s = 0
for i in range(n):
    start, end = merged_intervals[i]

    s += end - start + 1

print("Total covered ids:", s)

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

range_offset = 0
n = len(items)
m = len(merged_intervals)
spoiled = 0

for i in range(n):
    item = items[i]
    while range_offset < m - 1 and item > merged_intervals[range_offset][1]:
        range_offset += 1

    # print(
    #     "Considering item:",
    #     item,
    #     "Range:",
    #     merged_intervals[range_offset],
    #     "Offset:",
    #     range_offset,
    # )
    if (
        item < merged_intervals[range_offset][0]
        or item > merged_intervals[range_offset][1]
    ):
        spoiled += 1
        # print(f"Item {item} is spoiled")

print("Spoiled items:", spoiled)
print("Total fresh items:", n - spoiled)

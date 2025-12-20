import sys

INPUT_FILE = sys.argv[1]

ranges = []
with open(INPUT_FILE, "r") as f:
    ranges = [
        [x.split("-")[0], x.split("-")[1]] for x in f.read().strip("\n").split(",")
    ]

print(ranges)

s = 0
for r in ranges:
    start, end = int(r[0]), int(r[1]) + 1

    for i in range(start, end):
        sr = str(i)
        n = len(sr) // 2
        for j in range(n):
            if len(sr) % j != 0:
                continue

            if sr[:n] == sr[n:]:
                print("Invalid ID:", i)
                s += i

print("Final sum is:", s)

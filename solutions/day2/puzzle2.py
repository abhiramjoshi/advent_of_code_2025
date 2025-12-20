import sys

INPUT_FILE = sys.argv[1]

ranges = []
with open(INPUT_FILE, "r") as f:
    ranges = [
        [x.split("-")[0], x.split("-")[1]] for x in f.read().strip("\n").split(",")
    ]

print(ranges)

s = 0
invalids = set()
for r in ranges:
    start, end = int(r[0]), int(r[1]) + 1

    for i in range(start, end):
        sr = str(i)
        n = len(sr) // 2
        for j in range(1, n + 1):
            if len(sr) % j != 0:
                continue

            valid = False
            for k in range(1, len(sr) // j):
                if sr[:j] != sr[j * k : j * (k + 1)]:
                    valid = True
                    break

            if not valid:
                if i not in invalids:
                    print("Invalid ID:", i)
                    s += i
                    invalids.add(i)

print("Final sum is:", s)

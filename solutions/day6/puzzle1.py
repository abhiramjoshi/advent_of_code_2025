import sys

INPUT_FILE = sys.argv[1]

problems = []
with open(INPUT_FILE, "r") as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        row = line.split()
        n = len(row)
        if not problems:
            problems = [[] for _ in range(n)]

        for i in range(n):
            try:
                problems[i].append(int(row[i]))
            except ValueError:
                problems[i].append(row[i])

print(problems)

s = 0
n = len(problems)
for i in range(n):
    op = problems[i][-1]

    ans = problems[i][0]
    m = len(problems[i])
    for j in range(1, m - 1):
        if op == "*":
            ans *= problems[i][j]
        elif op == "+":
            ans += problems[i][j]

    s += ans

print("Solution:", s)

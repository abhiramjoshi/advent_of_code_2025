import sys

INPUT_FILE = sys.argv[1]
problems = []
with open(INPUT_FILE, "r") as f:
    problems = [line.rstrip("\n") for line in f.readlines()]

ops = problems[-1]
column_widths = []
width = 0
for b in ops:
    if b != " ":
        column_widths.append(width - 1)
        width = 0
    width += 1
column_widths.append(width)
column_widths.pop(0)
problems.pop(-1)
ops = ops.split()

s = 0
n = len(problems)
m = len(ops)

for i in range(n):
    row = []
    offset = 0
    for j in range(m):
        row.append(problems[i][offset : offset + column_widths[j]])
        offset += column_widths[j] + 1
    problems[i] = row

for j in range(m):
    op = ops[j]
    ans = 1 if op == "*" else 0
    for k in range(column_widths[j]):
        num = []
        for i in range(n):
            # print(problems[i][j], column_widths[j])
            num.append(problems[i][j][k])

        strint = "".join(num).strip()
        if not strint:
            continue

        if op == "*":
            ans *= int(strint)
        else:
            ans += int(strint)
    s += ans

print("Solution:", s)

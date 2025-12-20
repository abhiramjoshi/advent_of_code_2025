# Calculate the distance between all pairs, this is n^2 of 1000, equals 1000000
# calculations. Technically doable, maybe not the best, but doable.
# Add this to a min heap, and then take the top 1000 entries not in the same
# group after joining.
import sys
from heapq import heappush, heappop

INPUT_FILE = sys.argv[1]
NUM_PAIRS = int(sys.argv[2])

points = []
with open(INPUT_FILE, "r") as f:
    points = [list(map(int, line.rstrip("\n").split(","))) for line in f.readlines()]


# Calculate and push distances
distances = []
n = len(points)
for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]

        distance = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        heappush(distances, (distance, i, j))

# Pop from heap and group nodes. If part already part of the same node, skip
# (Create union-find datastructure)


class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def union(self, i, j):
        i_parent = self.find(i)
        j_parent = self.find(j)
        if i_parent == j_parent:
            return

        if self.size[i_parent] > self.size[j_parent]:
            self.parents[j_parent] = i_parent
            self.size[i_parent] += self.size[j_parent]
        elif self.size[i_parent] < self.size[j_parent]:
            self.parents[i_parent] = j_parent
            self.size[j_parent] += self.size[i_parent]
        else:
            if i_parent < j_parent:
                self.parents[j_parent] = i_parent
                self.size[i_parent] += self.size[j_parent]
            else:
                self.parents[i_parent] = j_parent
                self.size[j_parent] += self.size[i_parent]

    def find(self, i):
        parent = self.parents[i]
        if parent != i:
            parent = self.find(parent)
            self.parents[i] = parent
        return parent

    def __str__(self):
        return f"Parents: {self.parents}\nSizes: {self.size}"


circuits = UnionFind(n)

count = 0
while distances and count < NUM_PAIRS:
    count += 1
    _, n1, n2 = heappop(distances)
    p1 = circuits.find(n1)
    p2 = circuits.find(n2)
    if p1 == p2:
        continue

    circuits.union(n1, n2)

sizes = [circuits.size[i] for i in range(n) if circuits.parents[i] == i]
sizes.sort(reverse=True)
print("Size of largest circuits is:", sizes[0] * sizes[1] * sizes[2])

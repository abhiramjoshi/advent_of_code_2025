# This is a directed acyclical graph (has to be, as with cycles you cannot count
# paths), and we need to find all the paths in the graph from
# source to destination.

# Do recursive DFS + memoization to get number of paths
import sys
from functools import cache

INPUT_FILE = sys.argv[1]

graph = {}
with open(INPUT_FILE, "r") as f:
    for line in f.readlines():
        source, dests = line.rstrip("\n").split(":")
        graph[source] = dests.strip().split(" ")

print(graph)

graph["out"] = []


@cache
def recurse_count(node, dest, has_fft, has_dac):
    if node == dest:
        if has_dac and has_fft:
            return 1

    if node == "fft":
        has_fft = True

    if node == "dac":
        has_dac = True

    paths = 0

    for child in graph[node]:
        paths += recurse_count(child, dest, has_fft, has_dac)

    return paths


total = recurse_count("svr", "out", False, False)
print("Total paths with fft and dac:", total)

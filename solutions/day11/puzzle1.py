# This is a directed acyclical graph (has to be, as with cycles you cannot count
# paths), and we need to find all the paths in the graph from
# source to destination.

# Do recursive DFS + memoization to get number of paths
from functools import cache
import sys

INPUT_FILE = sys.argv[1]

graph = {}
with open(INPUT_FILE, "r") as f:
    for line in f.readlines():
        source, dests = line.rstrip("\n").split(":")
        graph[source] = dests.strip().split(" ")

print(graph)


@cache
def recurse_count(node, dest):
    if node == dest:
        return 1

    paths = 0

    for child in graph[node]:
        paths += recurse_count(child, dest)

    return paths


total_paths = recurse_count("svr", "out")

print("Total paths:", total_paths)

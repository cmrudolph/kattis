# NAME : Running MoM
# URL  : https://open.kattis.com/problems/runningmom
# =============================================================================
# Weighted graph problem where DFS can be used to identify cycles and the
# cycles serve as the basis for identifying "safe" cities in the analysis.
# =============================================================================

import sys
from collections import defaultdict


def dbg(str):
    print(str, file=sys.stderr)


def recurse(graph, all_visited, curr_visited, safe, curr_key):
    if curr_key in all_visited:
        return

    if curr_key in curr_visited:
        # Cycle detected. All cities participating in this cycle are safe.
        # This set consists of all cities between the first and second
        # sighting of the city we just noticed for a second time.
        seen_curr = False
        for s in curr_visited:
            if s == curr_key:
                seen_curr = True
            if seen_curr and s not in safe:
                safe.add(s)
        return

    # Recursively visit the connected nodes in the graph
    curr_visited.append(curr_key)
    if curr_key in graph:
        for dest in graph[curr_key]:
            recurse(graph, all_visited, curr_visited, safe, dest)
    curr_visited.pop()
    all_visited.add(curr_key)


def main():
    sys.setrecursionlimit(10000)
    next_idx = 0
    n = int(input())
    city_to_idx = dict()
    graph = defaultdict(set)
    for i in range(n):
        o, d = input().strip().split()

        # Map names to integers to make keyed lookups faster
        if not o in city_to_idx:
            city_to_idx[o] = next_idx
            next_idx += 1
        if not d in city_to_idx:
            city_to_idx[d] = next_idx
            next_idx += 1

        o_idx = city_to_idx[o]
        d_idx = city_to_idx[d]
        graph[o_idx].add(d_idx)

    all_visited = set()
    curr_visited = []
    safe = set()

    for key in graph:
        recurse(graph, all_visited, curr_visited, safe, key)

    for line in sys.stdin:
        line = line.strip()
        idx = city_to_idx[line]
        status = "safe" if idx in safe else "trapped"
        print(line, status)


if __name__ == "__main__":
    main()

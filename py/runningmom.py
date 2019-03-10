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


def recurse(graph, history, solved, curr):
    if curr in solved:
        return solved[curr]

    if curr in graph:
        for neighbor in graph[curr]:
            if neighbor in history:
                solved[neighbor] = True
                return True
            if recurse(graph, history | {neighbor}, solved, neighbor):
                solved[neighbor] = True
                return True

    solved[curr] = False
    return False


def main():
    sys.setrecursionlimit(10000)
    next_idx = 0
    n = int(input())
    city_to_idx = dict()
    graph = defaultdict(set)
    for i in range(n):
        o, d = input().strip().split()

        # Map names to integers to make keyed lookups faster
        if o not in city_to_idx:
            city_to_idx[o] = next_idx
            next_idx += 1
        if d not in city_to_idx:
            city_to_idx[d] = next_idx
            next_idx += 1

        o_idx = city_to_idx[o]
        d_idx = city_to_idx[d]
        graph[o_idx].add(d_idx)

    all_visited = set()
    curr_visited = []
    solved = dict()

    for line in sys.stdin:
        line = line.strip()
        idx = city_to_idx[line]
        history = {idx}
        safe = recurse(graph, history, solved, idx)
        status = "safe" if safe is True else "trapped"
        print(line, status)


if __name__ == "__main__":
    main()

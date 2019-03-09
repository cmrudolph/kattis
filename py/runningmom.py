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


def dfs(graph, all_visited, safe, start):
    # Iterative DFS to avoid recursion limits
    stack = [start]
    while len(stack) > 0:
        curr = stack[-1]
        if curr in all_visited:
            # Avoid redundant work.
            stack.pop()
        else:
            all_visited.add(curr)
            for neighbor in graph.get(curr, set()):
                if neighbor in stack:
                    # Found a cycle. All cities from the first sighting to
                    # the second sighting are considered safe.
                    idx = stack.index(neighbor)
                    for s in stack[idx:]:
                        safe.add(s)
                elif neighbor not in all_visited:
                    # Unvisited neighbor - push it to visit later.
                    stack.append(neighbor)


def main():
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
    safe = set()

    for start in graph:
        dfs(graph, all_visited, safe, start)

    for line in sys.stdin:
        line = line.strip()
        idx = city_to_idx[line]
        status = "safe" if idx in safe else "trapped"
        print(line, status)


if __name__ == "__main__":
    main()

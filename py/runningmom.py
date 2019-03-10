# NAME : Running MoM
# URL  : https://open.kattis.com/problems/runningmom
# =============================================================================
# Weighted graph problem where DFS can be used to identify cycles and the
# cycles serve as the basis for identifying "safe" cities in the analysis.
# Recursion doesn't fly here because of stack size limits, so an iterative
# approach is used. History tracking is required since we need to be able to
# trace the path we have taken when analyzing cycles.
# =============================================================================

import sys
from collections import defaultdict


def dbg(str):
    print(str, file=sys.stderr)


def dfs(graph, all_visited, safe, start):
    # Iterative DFS to avoid recursion limits
    stack = [(start, [start])]
    hist_set = {start}
    while len(stack) > 0:
        top = stack[-1]
        top_vertex = top[0]
        top_history = top[1]
        if top_vertex in all_visited:
            # Avoid redundant work.
            stack.pop()
        else:
            all_visited.add(top_vertex)
            for neighbor in graph.get(top_vertex, set()):
                if neighbor in hist_set:
                    cycle_detected = False
                    for hist in top_history:
                        if hist == neighbor:
                            # Found a cycle. All cities from the first sighting to
                            # the second sighting are considered safe.
                            cycle_detected = True
                        if cycle_detected:
                            if hist not in safe:
                                safe.add(hist)
                if neighbor not in all_visited:
                    # Unvisited neighbor - push it to visit later.
                    stack.append((neighbor, top_history + [neighbor]))
                    hist_set.add(neighbor)


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

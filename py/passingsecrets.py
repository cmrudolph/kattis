# NAME : Passing Secrets
# URL  : https://open.kattis.com/problems/passingsecrets
# =============================================================================
# Undirected, weighted graph problem where we want the shortest route between
# two specific nodes. Start by building the graph representation of the
# problem domain based on the inputs. Then apply Dijkstra's algorithm to
# identify the shortest paths from the starting node to everything else.
# Finally consult the search results to retrace our steps to get to the
# end node optimally.
# =============================================================================

import pprint
import sys
from collections import OrderedDict

# Close enough to infinity for our purposes
INF = 888888888


class Entry:
    visited = False
    cost = INF
    prev = None

    def __str__(self):
        return f"V:{self.visited}; C:{self.cost}; P:{self.prev}"


def dbg(str):
    print(str, file=sys.stderr)


def build_graph(groups, name_to_idx):
    # Represent as an adjacency list
    graph = [{} for n in name_to_idx]

    for g in groups:
        for i in range(len(g)):
            for j in range(i + 1, len(g)):
                # Calculate the weight of the undirected link and keep
                # track of the best one we have seen. The outcome of this
                # calculation is a complete, undirected, weighted graph
                # with every direct connection cost minimized.
                # COST = (group size - 2) + 1
                cost = (len(g) - 2) + 1
                name1 = g[i]
                name2 = g[j]
                idx1 = name_to_idx[name1]
                idx2 = name_to_idx[name2]

                # Found a cheaper path
                link1 = graph[idx1].get(idx2, None)
                if link1 is None or cost < link1:
                    graph[idx1][idx2] = cost
                    graph[idx2][idx1] = cost

    return graph


def calc_shortest_paths(graph):
    # Tracking structure for Dijkstra's algorithm
    entries = [Entry() for idx, e in enumerate(graph)]
    entries[0].cost = 0

    i = 0
    while True:
        entries[i].visited = True
        for conn_idx in graph[i]:
            if not entries[conn_idx].visited:
                old_cost = entries[conn_idx].cost
                new_cost = entries[i].cost + graph[i][conn_idx]
                if old_cost == INF or old_cost > new_cost:
                    entries[conn_idx].cost = new_cost
                    entries[conn_idx].prev = i

        # Pick next place to visit (min unvisited)
        i = None
        for idx, x in enumerate(entries):
            if not x.visited and (i is None or x.cost < entries[i].cost):
                i = idx

        if i is None:
            return entries


def print_best_route(entries, idx_to_name):
    if entries[1].cost == INF:
        # No path from 0 --> 1
        print("impossible")
    else:
        # Output the best path from 0 --> 1 by traversing the links
        i = 1
        cost = entries[i].cost
        final_names = []
        while i != 0:
            final_names.append(idx_to_name[i])
            i = entries[i].prev
        final_names.append(idx_to_name[0])
        final_names.reverse()

        # Adjust the cost because we technically overcounted the number of
        # intermediaries by one. We added 1 to each edge for simplicity, but
        # the number of intermediaries is EDGES - 1
        print(f"{cost - 1} {' '.join(final_names)}")


def main():
    for case in sys.stdin:
        # Search will always be from [0] to [1]
        target1, target2 = case.split()
        name_to_idx = OrderedDict()
        name_to_idx[target1] = None
        name_to_idx[target2] = None
        idx_to_name = {}

        n = int(input())
        groups = []
        for i in range(n):
            names = input().split()
            groups.append(names)
            for n in names:
                name_to_idx[n] = None

        # Now that we have a complete list of names, map each name to its
        # numeric index for instant lookups later on and map up the reverse
        # to resolve names in the end
        for idx, n in enumerate(name_to_idx):
            name_to_idx[n] = idx
            idx_to_name[idx] = n

        graph = build_graph(groups, name_to_idx)
        entries = calc_shortest_paths(graph)

        print_best_route(entries, idx_to_name)


if __name__ == "__main__":
    main()

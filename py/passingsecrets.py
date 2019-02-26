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


def main():
    for case in sys.stdin:
        # Search will always be from [0] to [1]
        target1, target2 = case.split()
        name_to_idx = OrderedDict()
        name_to_idx[target1] = -1
        name_to_idx[target2] = -1
        idx_to_name = {}

        n = int(input())
        groups = []
        for i in range(n):
            names = input().split()
            groups.append(names)
            for n in names:
                name_to_idx[n] = -1

        # Now that we have a complete list of names, map each name to its
        # numeric index for instant lookups later on and map up the reverse
        # to resolve names in the end
        for idx, n in enumerate(name_to_idx):
            name_to_idx[n] = idx
            idx_to_name[idx] = n

        # Represent the graph as a list of dictionaries (conceptually an
        # adjacency list)
        graph = [{} for n in name_to_idx]

        for g in groups:
            for i in range(len(g)):
                for j in range(i + 1, len(g)):
                    # Calculate the weight of the undirected link and keep
                    # track of the best one we have seen. The outcome of this
                    # calculation is a complete, undirected, weighted graph
                    # with every direct connection cost minimized
                    cost = len(g) - 2
                    name1 = g[i]
                    name2 = g[j]
                    idx1 = name_to_idx[name1]
                    idx2 = name_to_idx[name2]

                    # Found a cheaper path
                    link1 = graph[idx1].get(idx2, -1)
                    if link1 == -1 or cost < link1:
                        graph[idx1][idx2] = cost
                        graph[idx2][idx1] = cost

        # Tracking structure for Dijkstra's algorithm
        entries = [Entry() for e in graph]
        entries[0].cost = -1

        done = False
        curr = 0
        while not done:
            entries[curr].visited = True
            for conn_idx in graph[curr]:
                if not entries[conn_idx].visited:
                    old_cost = entries[conn_idx].cost
                    new_cost = entries[curr].cost + graph[curr][conn_idx] + 1
                    if old_cost == INF or old_cost > new_cost:
                        entries[conn_idx].cost = new_cost
                        entries[conn_idx].prev = curr

            # Pick next place to visit (min unvisited)
            curr = -1
            for i, x in enumerate(entries):
                if not x.visited:
                    if curr == -1 or (x.cost < entries[curr].cost):
                        curr = i

            if curr == -1:
                done = True

        # pprint.pprint(name_to_idx, stream=sys.stderr)
        # pprint.pprint(graph, stream=sys.stderr)

        # for i, val in enumerate(entries):
            # dbg(f"{i}: {val}")

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
            print(f"{cost} {' '.join(final_names)}")


if __name__ == "__main__":
    main()

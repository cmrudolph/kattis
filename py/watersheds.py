# NAME : Watersheds
# URL  : https://open.kattis.com/problems/watersheds
# =============================================================================
# Graph problem based on a 2D array concept. Cells are conditionally connected
# based on rules (relationships simulating height differences), which produce
# sets of distinct drainage basins. Said basins need to be identified and
# labeled. Solved by defining the graph using adjacency lists, then traversing
# and labeling contiguous sections.
# =============================================================================

import sys

# Valid range is 0 <= H <= 10000
UNDEFINED_HEIGHT = 20000

UNLABELED = -1

rows = -1
cols = -1
cells = -1


def dbg(str):
    print(str, file=sys.stderr)


def to_idx(row, col):
    global cols
    return (row * cols) + col


def visit_all(labels, adj_lists, idx, label):
    # Recursively visit all connected nodes, labeling them as we go
    if labels[idx] == UNLABELED:
        labels[idx] = label
        for connected in adj_lists[idx]:
            visit_all(labels, adj_lists, connected, label)


def main():
    global rows
    global cols

    cases = int(input())
    for i in range(cases):
        next_label = 'a'
        rows, cols = (int(x) for x in input().split())
        cells = rows * cols

        # Array holding the elevations of cells [1, 8, 17, etc.]
        heights = [-1 for x in range(cells)]
        for r in range(rows):
            row_values = [int(x) for x in input().split()]
            for c in range(cols):
                idx = to_idx(r, c)
                heights[idx] = row_values[c]

        # Adjacency lists to track connected nodes
        adj_lists = [[] for x in range(cells)]

        for r in range(rows):
            for c in range(cols):
                best_height = UNDEFINED_HEIGHT
                curr_idx = to_idx(r, c)
                curr_height = heights[curr_idx]

                # Neighbors are checked in priority order (N, W, E, S)
                to_check = []
                if r > 0:
                    to_check.append(to_idx(r - 1, c))
                if c > 0:
                    to_check.append(to_idx(r, c - 1))
                if c < cols-1:
                    to_check.append(to_idx(r, c + 1))
                if r < rows-1:
                    to_check.append(to_idx(r + 1, c))

                for neighbor_idx in to_check:
                    height = heights[neighbor_idx]
                    if height < curr_height and height < best_height:
                        best_height = height
                        best_idx = neighbor_idx

                if best_height != UNDEFINED_HEIGHT:
                    # Establish links in both directions to indicate that
                    # these cells are part of the same drainage basin
                    adj_lists[curr_idx].append(best_idx)
                    adj_lists[best_idx].append(curr_idx)

        # Array holding the final labels of cells [a, b, c, etc.]
        labels = [UNLABELED for x in range(cells)]

        # Make sure we visit every cell in our map
        for idx in range(cells):
            if labels[idx] == UNLABELED:
                visit_all(labels, adj_lists, idx, next_label)
                next_label = chr(ord(next_label) + 1)

        print(f"Case #{i + 1}:")
        for r in range(rows):
            vals = [labels[to_idx(r, c)] for c in range(cols)]
            print(" ".join(vals))


if __name__ == "__main__":
    main()

# https://open.kattis.com/problems/amoebas

# OK: Solution that works through the search space using recursion, tagging
# cells along the way. In principle, recursion can overflow the stack in these
# types of problems, but the search space here is sufficiently small that it
# is okay.

import sys

IGNORE = 0
NOT_VISITED = -1

next_tag = 1


def dbg(str):
    print(str, file=sys.stderr)


def matrix_to_str(matrix):
    return '\n'.join([''.join(['{:2}'.format(item) for item in row])
                      for row in matrix])


# Gets the tag from a neighbor if one has been assigned.
def get_neighbor_tag(tag_matrix, rows, cols, row, col):
    # Search space = all neighboring cells as long as they fall within
    # the bounds of the matrix:
    # [ ? | ? | ? ]
    # [ ? |   | ? ]
    # [ ? | ? | ? ]
    n_rows = [r for r in range(row-1, row+2) if r >= 0 and r < rows]
    n_cols = [c for c in range(col-1, col+2) if c >= 0 and c < cols]

    dbg(f"R:{row}; C:{col}; NR: {n_rows}; NC: {n_cols}")

    for r in n_rows:
        for c in n_cols:
            if tag_matrix[r][c] > 0:
                return tag_matrix[r][c]

    return 0


# Investigate a cell to see if it needs to be tagged. If we encounter a
# new cell needing a tag, we will also recursively process its neighbors
# immediately to make sure we do not miss links in the loop in our
# naive iterative traversal driving the whole process.
def investigate_cell(tag_matrix, rows, cols, row, col):
    global next_tag

    # Unprocessed black square. This is something we know we need
    # to investigate.
    if tag_matrix[row][col] == NOT_VISITED:
        dbg(f"Investigate -- R:{row}; C:{col}")
        tag = get_neighbor_tag(tag_matrix, rows, cols, row, col)
        if tag > 0:
            # Found a neighbor who:
            #   1. Is black
            #   2. Has already been visited (has a tag assigned)
            # Based on this we know we are part of the same loop and
            # must have the same tag.
            dbg(f"Tag -- T:{tag}; R:{row}; C:{col}")
            tag_matrix[row][col] = tag
        else:
            # No neighbors with significant tags. We are the first
            # cell to be visited in this loop. Assign a new tag.
            dbg(f"New -- T:{next_tag}; R:{row}; C:{col}")
            tag_matrix[row][col] = next_tag
            next_tag += 1

        n_rows = [r for r in range(row-1, row+2)
                  if r >= 0 and r < rows]
        n_cols = [c for c in range(col-1, col+2)
                  if c >= 0 and c < cols]

        for r in n_rows:
            for c in n_cols:
                investigate_cell(tag_matrix, rows, cols, r, c)


def main():
    info = input().split(" ")
    rows = int(info[0])
    cols = int(info[1])

    dbg(f"Rows:{rows}; Cols:{cols}")

    # tag_matrix indicates the amoeba tags we have assigned.
    #   -1 : Unprocessed black square
    #   0  : No tag needed (white)
    #   >0 : Tag we have set
    tag_matrix = [[IGNORE for c in range(cols)] for r in range(rows)]

    for r in range(rows):
        input_data = input()
        for c in range(cols):
            if input_data[c] == '#':
                # We found a black square. Whites are already initialized via
                # defaulting, but these need to be explicitly set up.
                tag_matrix[r][c] = NOT_VISITED

    # Walk through the entire matrix until ever cell has been looked at.
    for r in range(rows):
        for c in range(cols):
            investigate_cell(tag_matrix, rows, cols, r, c)

    dbg(matrix_to_str(tag_matrix))

    print(str(next_tag - 1))


if __name__ == "__main__":
    main()

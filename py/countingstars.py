# https://open.kattis.com/problems/countingstars

# OK: Similar problem to amoebas, but recursion grew the stack too much. Using
# iteration with a queue to visit and tag cells instead.

import sys

IGNORE = 0
NEEDS_VISIT = -1
STAR_CH = "-"


def q_neighbors(tag_matrix, rows, cols, r, c, q):
    # Range check stuff, see if the cell is unvisited, then queue it
    if r > 0:
        if tag_matrix[r-1][c] == NEEDS_VISIT:
            q.append((r-1, c))
    if r < (rows - 1):
        if tag_matrix[r+1][c] == NEEDS_VISIT:
            q.append((r+1, c))
    if c > 0:
        if tag_matrix[r][c-1] == NEEDS_VISIT:
            q.append((r, c-1))
    if c < (cols - 1):
        if tag_matrix[r][c+1] == NEEDS_VISIT:
            q.append((r, c+1))


def main():
    case = 1
    for line in sys.stdin:
        next_tag = 1
        info = line.split()
        rows = int(info[0])
        cols = int(info[1])

        tag_matrix = [[IGNORE for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            input_data = input()
            for c in range(cols):
                if input_data[c] == STAR_CH:
                    tag_matrix[r][c] = NEEDS_VISIT

        q = []
        for r in range(rows):
            for c in range(cols):
                if tag_matrix[r][c] == NEEDS_VISIT:
                    q.append((r, c))
                    while len(q) > 0:
                        q_r, q_c = q.pop(0)
                        if tag_matrix[q_r][q_c] == NEEDS_VISIT:
                            tag_matrix[q_r][q_c] = next_tag
                            q_neighbors(tag_matrix, rows, cols, q_r, q_c, q)

                    next_tag += 1

        print(f"Case {case}: {next_tag - 1}")
        case += 1


if __name__ == "__main__":
    main()

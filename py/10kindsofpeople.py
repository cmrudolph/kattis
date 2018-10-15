# https://open.kattis.com/problems/10kindsofpeople

# SLOW: Same algorithm as the C implementation. The Python version was simply
# too slow when run on the judging machines.

import sys

UNINITIALIZED = -1
BINARY_TODO = 0
DECIMAL_TODO = 1


def dbg(str):
    print(str, file=sys.stderr)


def matrix_to_str(matrix):
    return '\n'.join([''.join(['{}'.format(item) for item in row])
                      for row in matrix])


def queue_neighbors(matrix, rows, cols, r, c, val, q):
    if r > 0:
        if matrix[r-1][c] == val:
            q.append((r-1, c, val))
    if r < (rows - 1):
        if matrix[r+1][c] == val:
            q.append((r+1, c, val))
    if c > 0:
        if matrix[r][c-1] == val:
            q.append((r, c-1, val))
    if c < (cols - 1):
        if matrix[r][c+1] == val:
            q.append((r, c+1, val))


def main():
    size_line = input().split()
    rows = int(size_line[0])
    cols = int(size_line[1])

    next_tag = 2
    tag_text = ['', '']

    # matrix indicates the tags we have assigned.
    #   -1   : State before reading input
    #    0   : Binary (untagged)
    #    1   : Decimal (untagged)
    #    2+  : Tagged
    matrix = [[UNINITIALIZED for c in range(cols)] for r in range(rows)]

    # Read the input and store all the initial values in the matrix. These
    # values represent either binary or decimal cells.
    for r in range(rows):
        input_data = input()
        for c in range(cols):
            if int(input_data[c]) == BINARY_TODO:
                matrix[r][c] = BINARY_TODO
            else:
                matrix[r][c] = DECIMAL_TODO

    # Traverse the matrix processing any unprocessed cell we encounter.
    # Processing a cell also means we need to visit any unprocessed
    # neighbors bearing the same designation (decimal or binary) as the cell
    # that initiated the "go check the neighbors" request.
    q = []
    for r in range(rows):
        for c in range(cols):

            # If the cell is unprocessed
            if matrix[r][c] == BINARY_TODO or matrix[r][c] == DECIMAL_TODO:
                q.append((r, c, matrix[r][c]))

                # At the end we need to report not only whether the
                # cells are connected, but which 'type' of connection
                # exists. Since we are not storing the original matrix
                # until the end, let's just capture which case we are
                # in and keep that info in a simple list correlated to
                # the tags we generate.
                if matrix[r][c] == BINARY_TODO:
                    tag_text.append("binary")
                else:
                    tag_text.append("decimal")

                # Continue until we have searched all connected cells with
                # the same value
                while len(q) > 0:
                    q_r, q_c, val = q.pop(0)
                    if matrix[q_r][q_c] == val:
                        matrix[q_r][q_c] = next_tag

                        queue_neighbors(matrix, rows, cols, q_r, q_c, val, q)

                next_tag += 1

    dbg(matrix_to_str(matrix))

    num_cases = int(input())
    for case in range(num_cases):
        r1, c1, r2, c2 = map(lambda x: int(x) - 1, input().split())

        dbg("CASE: " + str(r1) + " " + str(c1) + " " + str(r2) + " " + str(c2))

        tag1 = matrix[r1][c1]
        tag2 = matrix[r2][c2]

        dbg("TAGS: " + str(tag1) + " " + str(tag2))

        if tag1 == tag2:
            print(tag_text[tag1])
        else:
            print("neither")


if __name__ == "__main__":
    main()

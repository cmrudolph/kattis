# https://open.kattis.com/problems/10kindsofpeople

import sys

UNINITIALIZED = -1
BINARY = 0
DECIMAL = 1


def queue_neighbors():
    pass


def main():
    size_line = input().split()
    rows = int(size_line[0])
    cols = int(size_line[1])

    # tag_map indicates the tags we have assigned.
    #   -1   : Cell that still needs to be visited + tagged
    #   Else : Tag value assigned to the cell + appropriate neighbors 
    tag_matrix = [[UNINITIALIZED for c in range(cols)] for r in range(rows)]

    for r in range(rows):
        input_data = input()
        for c in range(cols):
            if input_data[c] == BINARY:
                tag_matrix[r][c] = BINARY
            else:
                tag_matrix[r][c] = DECIMAL

    print(tag_matrix)


if __name__ == "__main__":
    main()

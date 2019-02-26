# NAME : ASCII Figure Rotation
# URL  : https://open.kattis.com/problems/asciifigurerotation
# =============================================================================
# Straightforward 2D array manipulation problem where we must adjust
# both coordinates and values by applying a 90 degree rotation to the source
# values.
# =============================================================================

import sys
import pprint


mapping = {
        "-": "|",
        "|": "-",
        "+": "+",
        " ": " "
    }


def dbg(str):
    print(str, file=sys.stderr)


def main():
    first = True
    for n in sys.stdin:
        rows = int(n)

        if rows == 0:
            return 0
        elif not first:
            print()
        first = False

        raw_rows = [input() for r in range(rows)]

        # Find the max width since the input dimensions are not uniform
        cols = max([len(r) for r in raw_rows])

        # Fill the source arrays (build a completed rectangle via padding to
        # simplify traversal)
        source = [list(raw_rows[r].ljust(cols)) for r in range(rows)]

        # Pre-allocate an empty destination array with rotated dimensions
        dest = [list("".ljust(rows)) for r in range(cols)]

        # Walk the source arrays adjusting the destination coordinates to
        # account for the desired 90 degree rotation. Also map each character
        # since the rotation modifies them in addition to their position
        dest_c = rows - 1
        for r in range(rows):
            for c in range(cols):
                orig_val = source[r][c]
                dest[c][dest_c] = mapping[orig_val]
            dest_c -= 1

        for r in dest:
            print("".join(r).rstrip())


if __name__ == "__main__":
    main()

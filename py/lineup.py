# NAME : Line Them Up
# URL  : https://open.kattis.com/problems/lineup
# =============================================================================
# Simple problem.
# =============================================================================

import sys


def main():
    is_increasing = True
    is_decreasing = True

    input()
    names = [line.rstrip() for line in sys.stdin]
    prevName = names[0]

    for name in names[1:]:
        currName = name
        is_increasing &= prevName < currName
        is_decreasing &= prevName > currName
        prevName = currName

    if is_increasing:
        print("INCREASING")
    elif is_decreasing:
        print("DECREASING")
    else:
        print("NEITHER")


if __name__ == "__main__":
    main()

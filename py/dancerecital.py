# https://open.kattis.com/problems/dancerecital

# SLOW: Same algorithm as the C++ solution using permutations, but runs too
# slowly in Python.

import itertools
import sys


def dbg(str):
    print(str, file=sys.stderr)


def main():
    MaxRoutines = 10
    MaxPerformers = 26

    routines = []

    total_routines = int(input())
    for i in range(total_routines):
        routines.append(set(input()))

    routines_range = list(range(total_routines))
    routines_range_minus_one = list(range(total_routines - 1))

    distances = [[0 for c in routines_range] for r in routines_range]

    for i in routines_range:
        for j in range(i + 1, total_routines):
            intersect = routines[i].intersection(routines[j])
            diffs = len(intersect)
            distances[i][j] = diffs
            distances[j][i] = diffs

    best = sys.maxsize

    # Check all routine permutations since N is small enough.
    for p in itertools.permutations(routines_range):
        if p[0] < p[-1]:
            # Only need to check half the permutations (those that are mirror
            # images of each other will yield the same results)
            changes = 0
            for i in routines_range_minus_one:
                diffs = distances[p[i]][p[i+1]]
                changes += diffs

                # Bail early if we know this path is not optimal.
                if (changes >= best):
                    break

            if changes < best:
                best = changes

            if best == 0:
                print("0")
                sys.exit(0)

    print(str(best))


if __name__ == "__main__":
    main()

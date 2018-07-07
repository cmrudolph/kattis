# https://open.kattis.com/problems/dancerecital

# Given a list of dance routines (sets of dancers), figure out the minimum
# number of "quick changes" required. A quick change is when a given dancer
# appears in back-to-back routines. Minimizing quick changes is accomplished
# by determining the optimal way to order the routines.
#
# Since the number of routines is <= 10, searching through all permutations
# is reasonable. A naive, exhaustive search of all permutations is avoided
# by introducing optimizations:
#   1. Cache comparison results we have already seen.
#   2. Abort a search once we are certain it cannot be optimal.

import itertools
import sys

DEBUG = False


def dbg(str):
    if DEBUG:
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

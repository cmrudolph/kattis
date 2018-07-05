# https://open.kattis.com/problems/lineup

# Given a list of names, determine what order they are in (or none). This is
# a very simple problem requiring only a single enumeration of the original
# list while maintaining state variables corresponding to the two special
# goal states (increasing/decreasing). At the end, if either of these state
# variables is still set, we know the conditions were satisfied.

import sys

is_increasing = True
is_decreasing = True

sys.stdin.readline()
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

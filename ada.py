# https://open.kattis.com/problems/ada

# Given N outputs of a function evaluated at evenly-spaced intervals, the
# goal is to figure out two things:
#   1. The minimum degree of the polynomial that will produce these outputs
#   2. The next value in the sequence
#
# The basis for the solution involves calculating the differences between
# adjacent items and knowing that this new sequence corresponds to a
# polynomial of one degree less (the function's derivative). Eventually this
# process will result in a sequence of identical values. This corresponds to
# the slope of the linear expression (degree = 1) and serves as the base case
# for our algorithm. Once we have arrived here, we work our way back up the
# stack, calculating the next value for each sequence (a simple calculation
# involving the previous last item and the value returned from the recursion).
# Upon arriving back at the top we will have computed the next value in the
# original sequence AND the depth of our recursion corresponds to the degree.

import sys

DEBUG = False


def dbg(str):
    if DEBUG:
        print(str)


def process_level(data):
    dbg("Process")

    # diffs will hold the differences between adjacent terms as we walk
    # through the input list. By definition this list's size will be one
    # less than the source list.
    diffs = [0 for d in range(len(data) - 1)]

    for idx, val in enumerate(data):
        # Enumerate the entire data (original) list here. However, the
        # constraint below serves to make sure we ignore the skip what
        # would be the last step in our enumeration (we are accessing two
        # slots at a time so we DO look at every element.
        if idx < len(diffs):
            diffs[idx] = data[idx + 1] - data[idx]

    dbg(f"Data: {data}")
    dbg(f"Diffs: {diffs}")

    # If every item in the diffs set is identical, we have hit the base
    # case and can begin our journey back up the stack.
    if (len(set(diffs))) == 1:
        base_return = (1, diffs[0])
        dbg(f"Base Ret: {base_return}")
        return base_return

    recursion_return = process_level(diffs)

    degree = recursion_return[0] + 1
    returned_difference = recursion_return[1]

    old_last = diffs[-1]
    new_last = returned_difference + old_last

    my_return = (degree, new_last)
    dbg(f"My Return: {my_return}")
    return my_return


# Ignore the first integer (tells us how many). We just want the values.
input_vals = [int(v) for v in (input().split()[1:])]
dbg(f"Orig:{input_vals}")

# Begin the recursion
final_returned = process_level(input_vals)

dbg(f"Final Ret: {final_returned}")

degree = final_returned[0]
returned_difference = final_returned[1]

# NewLast - OldLast = Returned
# (rearranging some terms)
# NewLast = Returned + OldLast
old_last = input_vals[-1]
new_last = returned_difference + old_last

dbg(f"Degree: {degree}")
dbg(f"New Last: {new_last}")

print(str(degree) + " " + str(new_last))

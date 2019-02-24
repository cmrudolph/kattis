# NAME : The Calculus of Ada
# URL  : https://open.kattis.com/problems/ada
# =============================================================================
# Simple recursive implementation with no significant performance requirements.
# =============================================================================

import sys


def dbg(str):
    print(str, file=sys.stderr)


def process_level(data):
    dbg("Process")

    # diffs will hold the differences between adjacent terms as we walk
    # through the input list. By definition this list's size will be one
    # less than the source list.
    diffs = [0 for d in range(len(data) - 1)]

    for idx, val in enumerate(data):
        # Enumerate the entire data (original) list here. However, the
        # constraint below serves to make sure we skip what would
        # be the last step in our enumeration (we are accessing two
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


def main():
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


if __name__ == "__main__":
    main()

# NAME : All Different Directions
# URL  : https://open.kattis.com/problems/alldifferentdirections
# =============================================================================
# Read distances and angles and use basic trig to calculate destinations.
# Average the destinations once all inputs have been processed.
# =============================================================================

import math
import sys


def dbg(str):
    print(str, file=sys.stderr)


def format_as_str(val):
    s = str(val).rstrip("0").rstrip(".")
    if not s:
        s = "0"
    return s


def main():
    for line in sys.stdin:
        n = int(line)
        dests = []
        if n == 0:
            return

        # Process the directions given by each person
        for i in range(n):
            vals = input().split()
            x = float(vals[0])
            y = float(vals[1])
            angle = float(vals[3])

            # Arbitrary number of walk/turn instructions coming up
            for i in range(4, len(vals), 2):
                instr = vals[i]
                amount = float(vals[i + 1])
                if instr == "walk":
                    # WALK: Use trig to calculate the new coordinates
                    x += amount * math.cos(math.radians(angle))
                    y += amount * math.sin(math.radians(angle))
                else:
                    # TURN: angle adjustment - matters for future walk steps
                    angle += amount
            dests.append((x, y))

        avg_x = round(sum([v[0] for v in dests]) / len(dests), 4)
        avg_y = round(sum([v[1] for v in dests]) / len(dests), 4)

        worst_dist = 0
        for dest in dests:
            x_diff_squared = (dest[0] - avg_x) ** 2
            y_diff_squared = (dest[1] - avg_y) ** 2
            dist = math.sqrt(x_diff_squared + y_diff_squared)
            if dist > worst_dist:
                worst_dist = dist

        worst_dist = round(worst_dist, 4)
        avg_x_str = format_as_str(avg_x)
        avg_y_str = format_as_str(avg_y)
        dist_str = format_as_str(worst_dist)
        print(avg_x_str, avg_y_str, dist_str)


if __name__ == "__main__":
    main()

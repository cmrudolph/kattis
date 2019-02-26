# NAME : Anagram Counting
# URL  : https://open.kattis.com/problems/anagramcounting
# =============================================================================
# Calculate the total as n! / (n<sub>1</sub>!n<sub>2</sub>!...n<sub>k</sub>!)
# where the denominator is the product of the factorials of the number of
# occurrences of each distinct character in the input sequence.
# =============================================================================

import math
import sys


def dbg(str):
    print(str, file=sys.stderr)


def main():
    for line in sys.stdin:
        line = line.strip()

        n = math.factorial(len(line))
        occurrences = {}
        for c in line:
            curr = occurrences.get(c, 0)
            occurrences[c] = curr + 1

        product = 1
        for key in occurrences:
            product *= math.factorial(occurrences[key])

        result = n // product
        # dbg(f"LINE:{line}; N:{n}; PROD:{product}; RES:{result}")
        print(result)


if __name__ == "__main__":
    main()

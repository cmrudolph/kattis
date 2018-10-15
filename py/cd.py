# https://open.kattis.com/problems/cd

# SLOW: Python solution using sets to keep track of who has which CDs. This
# solution is too slow.

import sys


def dbg(str):
    print(str, file=sys.stderr)


def main():
    lines = sys.stdin.readlines()
    idx = 0

    n, m = [int(s) for s in (lines[idx].rstrip().split())]
    idx += 1

    while n > 0 or m > 0:
        jack = set()
        duplicates = 0

        for i in range(n):
            cd = int(lines[idx])
            idx += 1
            jack.add(cd)

        for i in range(m):
            cd = int(lines[idx])
            idx += 1
            if cd in jack:
                duplicates = duplicates + 1

        print(str(duplicates))
        n, m = [int(s) for s in lines[idx].split()]
        idx += 1


if __name__ == "__main__":
    main()

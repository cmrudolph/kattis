# https://open.kattis.com/problems/whatdoesthefoxsay

import sys


def dbg(str):
    print(str, file=sys.stderr)


def main():
    n = int(input())

    for c in range(n):
        sounds = set()
        recording = input().split()

        for line in sys.stdin:
            line = line.rstrip()
            if line == "what does the fox say?":
                break

            # Build a set of all the non-fox sounds
            sounds.add(line.split()[-1])

        # Exclude words from the fox collection if they were uttered by
        # other animals.
        fox_sounds = [r for r in recording if r not in sounds]
        print(" ".join(fox_sounds))


if __name__ == "__main__":
    main()

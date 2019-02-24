# NAME : Eb Alto Saxophone Player
# URL  : https://open.kattis.com/problems/saxophone
# =============================================================================
# Simple problem.
# =============================================================================

import sys


def main():
    # Everything expressed as zero-based numbers [0-9] to make things easier.
    notes = {
        "c": [1, 2, 3, 6, 7, 8, 9],
        "d": [1, 2, 3, 6, 7, 8],
        "e": [1, 2, 3, 6, 7],
        "f": [1, 2, 3, 6],
        "g": [1, 2, 3],
        "a": [1, 2],
        "b": [1],
        "C": [2],
        "D": [0, 1, 2, 3, 6, 7, 8],
        "E": [0, 1, 2, 3, 6, 7],
        "F": [0, 1, 2, 3, 6],
        "G": [0, 1, 2, 3],
        "A": [0, 1, 2],
        "B": [0, 1]
    }

    cases = int(input())
    for case in range(cases):
        presses = [0 for i in range(10)]
        pressed = [0 for i in range(10)]

        song = input()
        for ch in song:
            note_fingers = notes[ch]

            for i in range(10):
                pressed_for_this_note = i in note_fingers
                if pressed[i] == 0:
                    if pressed_for_this_note:
                        # NO -> YES: Press it down and count it
                        pressed[i] = 1
                        presses[i] = presses[i] + 1
                else:
                    if not pressed_for_this_note:
                        # YES -> NO: Release it
                        pressed[i] = 0

        print(" ".join([str(p) for p in presses]))


if __name__ == "__main__":
    main()

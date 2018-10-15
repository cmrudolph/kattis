# https://open.kattis.com/problems/acm

# OK: This problem has no performance issues, so Python is adequate.

import sys


def main():
    time = 0
    solved_probs = set()
    wrong_attempts = {}

    for d in (line.rstrip() for line in sys.stdin):
        if d == "-1":
            print(str(len(solved_probs)) + " " + str(time))
        else:
            (sub_time, problem, result) = d.split(" ")
            if result == "right":
                solved_probs.add(problem)
                time += int(sub_time)
                wrong_for_this = wrong_attempts.get(problem, 0)
                time += 20 * wrong_for_this
            else:
                wrong_attempts[problem] = wrong_attempts.get(problem, 0) + 1


if __name__ == "__main__":
    main()

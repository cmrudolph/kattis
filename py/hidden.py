# https://open.kattis.com/problems/hidden

# OK: Simple problem.

import sys


def main():
    password, message = input().split()
    pass_list = list(password)
    pass_set = set(pass_list)

    for c in message:
        if c == pass_list[0]:
            # Good = current char matches the first char in our shrinking
            # password list
            pass_list.pop(0)
            pass_set = set(pass_list)
        elif c in pass_set:
            # Done (failure) = current char is not what we are looking for AND
            # is not benign (it is in the password set)
            print("FAIL")
            sys.exit(0)

        if len(pass_list) == 0:
            # Done (success) = found everything we needed without hitting
            # a failure case first
            print("PASS")
            sys.exit(0)

    # Done (failure) = Walked entire message and did not find everything
    print("FAIL")


if __name__ == "__main__":
    main()

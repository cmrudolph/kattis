# https://open.kattis.com/problems/phonelist

import sys


def dbg(str):
    print(str, file=sys.stderr)


# Consistency is met if no phone number in the list is the prefix of another.
# Since we are working with a sorted list, we only need to compare adjacent
# items (is the previous item a prefix of the current one?)
def is_consistent(numbers):
    for j in range(1, len(numbers)):
        prev = numbers[j - 1]
        curr = numbers[j]

        if curr.startswith(prev):
            return "NO"

    return "YES"


def main():
    num_cases = int(input())
    for i in range(num_cases):
        numbers = []
        num_numbers = int(input())

        for j in range(num_numbers):
            numbers.append(input())

        # Sorting is necessary to make the later comparison logic simple.
        numbers.sort()

        print(is_consistent(numbers))


if __name__ == "__main__":
    main()

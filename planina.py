# https://open.kattis.com/problems/planina

import math


def main():
    n = int(input())

    to_raise = 3
    for i in range(2, n + 1):
        to_raise += math.pow(2, i-1)

    result = math.pow(to_raise, 2)
    print(math.trunc(result))


if __name__ == "__main__":
    main()

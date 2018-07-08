# https://open.kattis.com/problems/batterup


def main():
    input()

    at_bats = [int(a) for a in input().split() if a != "-1"]
    print(sum(at_bats) / len(at_bats))


if __name__ == "__main__":
    main()

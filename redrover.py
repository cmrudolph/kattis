# https://open.kattis.com/problems/redrover

import sys


def dbg(str):
    print(str, file=sys.stderr)


def main():
    message = input()
    substrs = set()
    dbg(f"Msg:{message}")

    # Walk through the possible subsequence lengths and build up a set
    # containing all possible subsequences.
    min_sublen = 2

    # It is only necessary to check substrings up to half the original
    # message's length. Anything longer would produce a less optimal result
    # than the unmodified string.
    max_sublen = len(message) // 2

    for sublen in range(2, max_sublen + 1):
        for start_idx in range(len(message) - sublen + 1):
            substr = message[start_idx:start_idx + sublen]
            substrs.add(substr)

    # Try out each substring until we find the best one.
    best_len = len(message)
    for s in substrs:
        modified = message.replace(s, "M")
        final_len = len(modified) + len(s)
        dbg(f"Check -- Substr:{s}; Len:{final_len}; Mod:{modified}")

        if final_len < best_len:
            dbg(f"New Best -- S:{s}; Len:{final_len}; Mod:{modified}")
            best_len = final_len

    print(str(best_len))


if __name__ == "__main__":
    main()

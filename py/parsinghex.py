# https://open.kattis.com/problems/parsinghex

# Extract hex strings using a regex.

import sys
import re


def main():
    r = re.compile('0x[0-9a-f]+', re.IGNORECASE)
    for line in sys.stdin:
        for hex_val in r.findall(line):
            # Convert each hex match to decimal and print
            dec_val = str(int(hex_val[2:], 16))
            print(hex_val + " " + dec_val)


if __name__ == "__main__":
    main()

# https://open.kattis.com/problems/calculator

# Leverage Python's eval function to make this simple.

import sys

for line in sys.stdin:
    print('{:0.2f}'.format(round(eval(line), 2)))
# https://open.kattis.com/problems/drmmessages

# OK: Straightforward application of the string manipulation rules. No
# performance constraints, so Python is adequate.

import sys

Offset = 65


# Get the character value represented by an index in the [0, 25] range.
def idx_to_ch(idx):
    return chr((idx % 26) + Offset)


# Get the value of a character in the range [0, 25].
def ch_to_idx(ch):
    return ord(ch) - Offset


# Get the rotation value of a string by adding up the index value [0, 25]
# for each character contained in it.
def calc_string_rotation(s):
    return sum(ch_to_idx(c) for c in s)


# Convert a character to a different one by rotating it by the specified
# number of spaces. This must account for wrapping around the alphabet.
def rotate_char(c, amount):
    return idx_to_ch(ch_to_idx(c) + amount)


# Rotate each character in a string by a specified number of spaces. This
# must account for wrapping around the alphabet.
def rotate_string(s, amount):
    return ''.join(rotate_char(c, amount) for c in s)


def main():
    in_str = input()

    # STEP1: DIVIDE. Just cut the string in half.
    mid = len(in_str) // 2
    split1 = in_str[:mid]
    split2 = in_str[mid:]

    # STEP2: ROTATE. Calculate the rotation amount for each half and then
    # perform the rotations.
    rot1 = calc_string_rotation(split1)
    rot2 = calc_string_rotation(split2)

    rotated1 = rotate_string(split1, rot1)
    rotated2 = rotate_string(split2, rot2)

    # STEP3: MERGE. Walk the strings together and let each character from
    # the second string define the rotation amount for the corresponding
    # character in the first string.
    final = []
    for ch1, ch2 in zip(rotated1, rotated2):
        amount = ch_to_idx(ch2)
        mod = rotate_char(ch1, amount)
        final.append(mod)

    print(''.join(final))


if __name__ == "__main__":
    main()

# https://open.kattis.com/problems/keytocrypto

# Given a string representing ciphertext and a secret, apply the rules of the
# problem to determine the original plaintext. The encryption algorithm
# is based on an autokey cipher and involves the secret being prepended to
# the original plaintext and extra characters truncated to generate the key.
# The key is then used as the basis for a per-character cyclic shift.
#
# The implementation is straightforward. We simple need to iterate over the
# ciphertext deriving the plaintext for each character. The secret gives
# us enough to derive the first S plaintext characters, after which we use
# the newly-generated plaintext characters as our key values.
#
# EXAMPLE: C1-C3 are used to derive P1-P3. P1-P3 serve as the key values for
# the next 3 characters we derive. And so on...
#   KEY : S1 S2 S3 P1 P2 P3
#   CT  : C1 C2 C3 C4 C5 C6
#   -----------------------
#   PT  : P1 P2 P3 P4 P5 P6

import sys

Offset = 65
DEBUG = False


def dbg(str):
    if DEBUG:
        print(str, file=sys.stderr)


# Get the character value represented by an index in the [0, 25] range.
def idx_to_ch(idx):
    return chr((idx % 26) + Offset)


# Get the value of a character in the range [0, 25].
def ch_to_idx(ch):
    return ord(ch) - Offset


ciphertext = input()
secret = input()

dbg(f"CT: {ciphertext}")
dbg(f"SECRET: {secret}")

key = secret
decrypted = ""
for idx, cipher_ch in enumerate(ciphertext):
    key_ch = key[idx]
    cipher_idx = ch_to_idx(cipher_ch)
    shift_amount = ch_to_idx(key_ch)
    plaintext_idx = cipher_idx - shift_amount
    plaintext_ch = idx_to_ch(plaintext_idx)

    dbg(f"Idx:{idx}; CIdx:{cipher_idx}; KeyCh:{key_ch}; " +
        f"ShiftAmt:{shift_amount}; PCh:{plaintext_ch}")
    decrypted += plaintext_ch
    key += plaintext_ch

print(decrypted)

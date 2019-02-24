# NAME : The Key to Cryptography
# URL  : https://open.kattis.com/problems/keytocrypto
# =============================================================================
# Straightforward application of the string manipulation rules. No
# performance constraints, so Python is adequate.
# =============================================================================

import sys

Offset = 65


def dbg(str):
    print(str, file=sys.stderr)


# Get the character value represented by an index in the [0, 25] range.
def idx_to_ch(idx):
    return chr((idx % 26) + Offset)


# Get the value of a character in the range [0, 25].
def ch_to_idx(ch):
    return ord(ch) - Offset


def main():
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


if __name__ == "__main__":
    main()

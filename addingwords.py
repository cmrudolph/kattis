# https://open.kattis.com/problems/addingwords

import sys


def dbg(str):
    print(str, file=sys.stderr)


def main():
    vals_to_terms = dict()
    terms_to_vals = dict()

    for line in sys.stdin:
        words = line.strip().split(' ')
        action = words[0]

        if action == "def":
            term = words[1]
            val = int(words[2])

            # One term can map to a given value at a time. If one already
            # exists, it needs to be removed
            old_term = vals_to_terms.get(val, None)
            if old_term is not None:
                del terms_to_vals[old_term]

            old_val = terms_to_vals.get(term, None)
            if old_val is not None:
                del vals_to_terms[old_val]

            vals_to_terms[val] = term
            terms_to_vals[term] = val

        elif action == "calc":
            expr_list = words[1:-1]
            found_unknown = False

            # The expression we want to evaluate excludes the first and last
            # items in the calc string ("calc" and "="). We also only need
            # to substitute terms in the even slots (the odd slots are filled
            # with operators).
            dbg("TTV: " + str(terms_to_vals))
            for i in range(0, len(expr_list), 2):
                term = expr_list[i]
                val = terms_to_vals.get(term, "unknown")
                if val == "unknown":
                    dbg("Unknown term: " + term)
                    found_unknown = True
                expr_list[i] = val

            if found_unknown:
                print(' '.join(words[1:]) + " unknown")
            else:
                result_val = eval(' '.join(map(lambda x: str(x), expr_list)))
                result_term = vals_to_terms.get(result_val, "unknown")
                print(' '.join(words[1:]) + " " + str(result_term))

        elif action == "clear":
            vals_to_terms.clear()
            terms_to_vals.clear()


if __name__ == "__main__":
    main()

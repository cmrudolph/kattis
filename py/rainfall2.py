# NAME : Rain Fall
# URL  : https://open.kattis.com/problems/rainfall2
# =============================================================================
# Interesting problem where we piece together the formula, then run
# a guess through it, compare, and refine the guess. Repeating this enough
# times gets us to right value for our unknown.
# =============================================================================

import sys

ITERATIONS = 1000


def dbg(str):
    print(str, file=sys.stderr)


def main():
    leak_level, leak_rate, t1, t2, obs = [float(x) for x in input().split()]

    # If we are below the leak, we know EXACTLY how much rain fell
    if obs < leak_level:
        print(f"{obs:.6f} {obs:.6f}")
        sys.exit(0)

    # If we are exactly at the leak level, we are confident that value is
    # our minimum (it was at least this much).
    min_rain = None
    if obs == leak_level:
        min_rain = obs

    low = obs
    high = 10000000
    guess = high

    # Run the guess/compare/refine loop enough times to get an accurate result
    for i in range(ITERATIONS):
        rate = guess / t1
        t1_pre_leak = leak_level / rate
        t1_leaking = t1 - t1_pre_leak
        t1_end_total = (t1_pre_leak * rate) + (t1_leaking * (rate - leak_rate))
        left_to_leak = max(t1_end_total - leak_level, 0)
        leak_after_rain = min(left_to_leak, t2 * leak_rate)

        obs_guess = t1_end_total - leak_after_rain
        dbg(f"R:{rate:.3f}; T1PL:{t1_pre_leak:.3f}; T1L:{t1_leaking:.3f}; " +
            f"T1ET:{t1_end_total:.3f}; LTL:{left_to_leak:.3f}; " +
            f"LAR:{leak_after_rain:.3f}; LOW:{low:.3f}; " +
            f"HIGH:{high:.3f}; CURR:{guess:.3f}; OBS:{obs_guess:.3f}")

        if obs_guess > obs:
            # Too high - lower the guess
            high = guess
            guess = (high + low) / 2
        else:
            # Too low - raise the guess
            low = guess
            guess = (high + low) / 2

    if min_rain is None:
        min_rain = guess

    print(f"{min_rain:.6f} {guess:.6f}")


if __name__ == "__main__":
    main()

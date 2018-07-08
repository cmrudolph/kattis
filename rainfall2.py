# https://open.kattis.com/problems/rainfall2

import sys

ITERATIONS = 1000


def dbg(str):
    print(str, file=sys.stderr)


def main():
    leak_level, leak_rate, t1, t2, obs = [float(x) for x in input().split()]

    # If we are below the leak, we know exactly how much rain fell
    if obs < leak_level:
        print(f"{obs:.6f} {obs:.6f}")
        sys.exit(0)

    min_rain = None
    if obs == leak_level:
        min_rain = obs

    low = obs
    high = 10000000
    guess = high

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
            high = guess
            guess = (high + low) / 2
        else:
            low = guess
            guess = (high + low) / 2

    if min_rain is None:
        min_rain = guess

    print(f"{min_rain:.6f} {guess:.6f}")


if __name__ == "__main__":
    main()

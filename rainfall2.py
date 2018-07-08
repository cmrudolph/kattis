# https://open.kattis.com/problems/rainfall2

import sys

ITERATIONS = 10000

def main():
    leak, leak_rate, t1, t2, obs = map(lambda x: float(x), input().split())

    # If we are below the leak, we know exactly how much rain fell
    if obs < leak:
        print(f"{obs:.6f} {obs:.6f}")
        sys.exit(0)

    min_rain = None
    if obs == leak:
        min_rain = obs

    low = obs
    high = 10000000
    curr = low

    for i in range(ITERATIONS):
        rain_rate_guess = curr / t1
        t1_not_leaking = leak / rain_rate_guess
        t1_leaking = t1 - t1_not_leaking
        t1_end_total = (t1_not_leaking * rain_rate_guess) + (t1_leaking * (rain_rate_guess - leak_rate))
        left_to_leak = max(t1_end_total - leak, 0)
        leak_after_rain = min(left_to_leak, t2 * leak_rate)

        obs_guess = t1_end_total - leak_after_rain
        # print(f"RR:{rain_rate_guess:.3f}; T1NL:{t1_not_leaking:.3f}; T1L:{t1_leaking:.3f}; T1ET:{t1_end_total:.3f}; LTL:{left_to_leak:.3f}; LAR:{leak_after_rain:.3f}; LOW:{low:.3f}; HIGH:{high:.3f}; CURR:{curr:.3f}; OBS:{obs_guess:.3f}", file=sys.stderr)

        if obs_guess > obs:
            high = curr
            curr = (high + low) / 2
        else:
            low = curr
            curr = (high + low) / 2

    if min_rain is None:
        min_rain = curr

    print(f"{min_rain:.6f} {curr:.6f}")

if __name__ == "__main__":
    main()


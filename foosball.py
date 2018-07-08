# https://open.kattis.com/problems/foosball

import sys


def dbg(str):
    print(str, file=sys.stderr)


def main():
    player_count = int(input())
    players = input().split()
    result_str = input()

    dbg(f"PlayerCount:{player_count}")
    dbg(f"Players:{players}")
    dbg(f"ResultStr:{result_str}")

    sides = [
        [players[0], players[2]],
        [players[1], players[3]]
    ]
    line = players[4:]

    dbg(f"Side[0]:{sides[0]}")
    dbg(f"Side[1]:{sides[1]}")
    dbg(f"Line:{line}")

    win_tracking = [
        [" ".join(sides[0][:]), 0],
        [" ".join(sides[1][:]), 0]
    ]

    best = 0
    dynasties = []

    for c in result_str:
        winner_idx = 0 if c == "W" else 1
        loser_idx = 1 if winner_idx == 0 else 0

        winner = sides[winner_idx]
        winner_rec = win_tracking[winner_idx]
        loser = sides[loser_idx]
        loser_rec = win_tracking[loser_idx]

        winner[0], winner[1] = winner[1], winner[0]
        winner_rec[1] += 1
        dbg(f"Win -- Team:{winner_rec[0]}; Wins:{winner_rec[1]}")

        if winner_rec[1] > best:
            best = winner_rec[1]
            dynasties = [winner_rec[0]]
            dbg(f"New Best -- Team:{winner_rec[0]}, Wins:{winner_rec[1]}")
        elif winner_rec[1] == best:
            dynasties.append(winner_rec[0])
            dbg(f"New Tie -- Team:{winner_rec[0]}, Wins:{winner_rec[1]}")

        line.append(loser[1])
        loser[1] = loser[0]
        loser[0] = line.pop(0)
        win_tracking[loser_idx] = [loser[1] + " " + loser[0], 0]
        dbg(f"New Losing Team: {win_tracking[loser_idx][0]}")

    print("\n".join(dynasties))


if __name__ == "__main__":
    main()

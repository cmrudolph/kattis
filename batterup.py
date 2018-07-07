# https://open.kattis.com/problems/batterup

input()
at_bats = map(lambda x: int(x), input().split())
filtered = [a for a in at_bats if a != -1]
print(sum(filtered) / len(filtered))

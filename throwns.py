# https://open.kattis.com/problems/throwns

from collections import deque


students, commands = (int(s) for s in input().split())

q = deque()
curr = 0
q.append(curr)

is_undo = False
for cmd in input().split():
    if cmd == "undo":
        is_undo = True
    elif is_undo:
        is_undo = False
        amount = int(cmd)
        for i in range(amount):
            q.pop()
        curr = q[-1]
    else:
        amount = int(cmd)
        new = (curr + amount) % students
        q.append(new)
        curr = new

print(str(q.pop()))

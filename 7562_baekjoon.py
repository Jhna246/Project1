from collections import deque
import sys

for _ in range(int(input())):
    n = int(sys.stdin.readline())
    s_x, s_y = map(int, sys.stdin.readline())
    e_x, e_y = map(int, sys.stdin.readline())

    visited = [[False for _ in range(n + 1)] for i in range(n + 1)]

    q = deque()
    q.append((s_x, s_y, 0))

    while q:
        new_x, new_y, val = q.popleft()
        if visited[new_x][new_y]:
            continue
        else:
            visited[new_x][new_y] = True
        if new_x == e_x and new_y == e_y:
            print(val)
            exit()
        else:
            for i in ():
                if i >= 0 and i <= 100000:
                    q.append((i, val + 1))

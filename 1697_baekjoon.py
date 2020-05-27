from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
visited = [False for _ in range(100000 + 1)]

q = deque()
q.append((n, 0))

while q:
    new_n, val = q.popleft()
    if visited[new_n]:
        continue
    else:
        visited[new_n] = True
    if new_n == k:
        print(val)
        exit()
    else:
        for i in (new_n - 1, new_n + 1, new_n * 2):
            if i >= 0 and i <= 100000:
                q.append((i, val + 1))
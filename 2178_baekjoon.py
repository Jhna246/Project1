from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
maze = [input() for _ in range(n)]
visited = [[False for _ in range(m)] for i in range(n)]
q = deque()
q.append((0, 0, 1))
visited[0][0] = True

n -= 1
m -= 1

while q:
    n_x, n_y, t = q.popleft()

    if n_x == n - 1 and n_y == m - 1:
        print(t)
        exit()
    else:
        for new_x, new_y in [(n_x - 1, n_y), (n_x + 1, n_y), (n_x, n_y + 1), (n_x, n_y - 1)]:
            if 0 <= new_x <= n and 0 <= new_y <= m and maze[new_x][new_y] == '1' and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                q.append((new_x, new_y, t + 1))

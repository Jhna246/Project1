from collections import deque
n, m = map(int, input().split())
sx, sy = map(int, input().split())
l, r = map(int, input().split())
sx-=1
sy-=1
lab = [input() for _ in range(n)]
visited = [[-1 for j in range(m)] for i in range(n)]
q = deque()
def go(x, y, s, lf=False):
    if 0<=x<n and 0<=y<m and lab[x][y] == '.' and visited[x][y] == -1:
        visited[x][y] = s
        if lf:
            q.appendleft((x, y))
        else:
            q.append((x,y))
ans = 0
go(sx, sy, 0)
while q:
    n_x, n_y = q.popleft()
    s = visited[n_x][n_y]
    ans += s + n_y - sy <= r*2 and s - n_y + sy <= l*2
    go(n_x-1, n_y, s, True)
    go(n_x +1, n_y, s , True)
    go(n_x, n_y -1, s+1)
    go (n_x, n_y + 1, s + 1)
print(str(ans))
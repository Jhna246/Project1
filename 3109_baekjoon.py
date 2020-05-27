n, m = map(int, input().split())
maze = [['x'] * m ]+ [list(input()) for _ in range(n)] + [['x'] * m ]
ans = 0
pipe = False


def dfs(row, col):
    global ans, pipe
    maze[row][col] = 'x'
    if col == m-1:
        pipe = True
        ans += 1
        return
    for drow in (-1, 0, 1):
        if maze[row+drow][col+1] == '.':
            dfs(row + drow, col + 1)
            if pipe:
                return


for i in range(1, n+1):
    pipe = False
    dfs(i, 0)

print(ans)
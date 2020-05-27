from collections import deque
import sys


def location(a, b):
    if board[a][b]:
        q.append(board[a][b])
        board[a][b] = 0


def move(n):
    # move left
    if n == 0:
        for a in range(t):
            for b in range(t):
                location(a, b)
            merge()


def merge(row, col, x, y):
    while q:
        x = q.popleft()
        if board[row][col] == 0:
            board[row][col] = x
        elif board[row][col] == x:
            board[row][col] = x * x


def solve(counter):
    global ans
    if counter == 5:
        for i in range(t):
            ans = max(ans, board[i])
    for n in range(4):
        move(n)
        solve(counter + 1)



t = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split()) for _ in range(t))]
q = deque()
ans = 0


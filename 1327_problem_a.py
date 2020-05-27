import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    if n - k ** 2 >= 0 and (n - k ** 2) % 2 == 0:
        print('YES')
    else:
        print('NO')

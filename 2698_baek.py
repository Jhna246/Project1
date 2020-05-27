import sys


dp = [[[0 for i in range(2)] for j in range(101)]for k in range(101)]
dp[1][0][1] = 1
dp[1][0][0] = 1

first = int(sys.stdin.readline())

while first > -1:
    n, k = map(int, sys.stdin.readline().split())
    for i in range(2, 101):
        for j in range(i):
            dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
            dp[i][j][1] = dp[i-1][j][0] + dp[i-1][j-1][1]
    print(sum(dp[n][k]))

    first -= 1
    if first == 0:
        exit()


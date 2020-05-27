import sys

n = int(sys.stdin.readline())
ans = 0
dp = [[0 for _ in range(12)] for i in range(100)]

if 0 < n <= 100:
    for i in range(2, 11):
        dp[0][i] = 1

    for j in range(1, n):
        dp[j][0] = 0
        dp[j][11] = 0
        for k in range(1, 11):
            dp[j][k] = (dp[j - 1][k - 1] + dp[j - 1][k + 1]) % 1000000000

    for a in range(1, 11):
        ans = (ans + dp[n - 1][a]) % 1000000000

    print(dp)
    print(ans)

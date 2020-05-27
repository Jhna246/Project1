import sys
sys.setrecursionlimit(100000)


def f(i, bit):
    if i == -1:
        return 0

    if i == 0:
        return bit == 0

    if dp[i][bit] != -1:
        return dp[i][bit]

    # 0000 (0), 0011 (3), 0110 (6), 1001 (9), 1100 (12)
    if bit == 0:
        dp[i][bit] = f(i - 2, 0) + f(i - 1, 0) + f(i - 1, 3) + f(i - 1, 6) + f(i - 1, 12)
        return dp[i][bit]

    if bit == 3:
        dp[i][bit] = f(i - 1, 0) + f(i - 1, 12)
        return dp[i][bit]

    if bit == 6:
        dp[i][bit] = f(i - 1, 9) + f(i - 1, 0)
        return dp[i][bit]

    if bit == 9:
        dp[i][bit] = f(i - 1, 6)
        return dp[i][bit]

    if bit == 12:
        dp[i][bit] = f(i - 1, 0) + f(i - 1, 3)
        return dp[i][bit]


t = int(sys.stdin.readline())
dp = [[-1 for k in range(16)] for l in range(100000)]

for j in range(t):
    n = int(sys.stdin.readline())
    # print(dp)
    print(f(n, 0))


import sys


def f(cur, mask):
    if cur == 11:
        return 0

    if dp[mask] != -1:
        return dp[mask]

    ans = -9e9
    for i in range(11):
        if not (mask & (1 << i)) and mat[cur][i]:
            print(mat[cur][i])
            ans = max(ans, mat[cur][i] + f(cur + 1, mask | (1 << i)))
    dp[mask] = ans
    return ans


for j in range(int(sys.stdin.readline())):
    mat = [[] for i in range(11)]
    dp = [-1] * (1 << 14)
    for i in range(11):
        mat[i] = list(map(int, sys.stdin.readline().split()))
    print(f(0, 0))
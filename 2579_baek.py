n = int(input())
dp = [[] for _ in range(2)]

dp[0].append(0)
dp[0].append(0)
dp[1].append(0)
dp[1].append(0)

for i in range(2, n + 2):
    stair = int(input())
    dp[0].append(dp[1][i-1] + stair)
    print(dp)
    dp[1].append(max(dp[1][i-2], dp[0][i-2]) + stair)
ans = max(dp[0][n+1], dp[1][n+1])
print(ans)
print(dp)
# import sys
#
# values = []
# dp = [0] * 10001
#
# first = int(sys.stdin.readline())
#
# for i in range(first):
#     n = int(sys.stdin.readline())
#     values.append(n)
#
# if first >= 1:
#     dp[0] = values[0]
# elif first >= 2:
#     dp[1] = values[0] + values[1]
# elif first >= 3:
#     dp[2] = max(values[0] + values[2], values[1] + values[2])
#
# for i in range(first):
#     dp[i] = max(dp[i-3] + values[i] + values[i-1], dp[i-2] + values[i])
#
# print(max(dp))


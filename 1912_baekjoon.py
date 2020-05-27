# import sys
#
# t = int(sys.stdin.readline())
# value = list(map(int, sys.stdin.readline().split()))
# dp = []
#
#
# for i in range(0, len(value)):
#     # print(i)
#     # print(value[i])
#     dp.append(value[i])
#     for j in range(i + 1, len(value)):
#         # print(dp[len(dp) - 1], value[j], 'sum val')
#         dp.append(dp[len(dp) - 1] + value[j])
#         # print(dp)
#
# print(max(dp))
# # print(value)

import sys

t = int(sys.stdin.readline())
value = list(map(int, sys.stdin.readline().split()))
dp = []
dp.append(value[0])

for i in range(len(value) - 1):
    # print(value[i + 1], dp[i], 'val, dp')
    dp.append(max(dp[i] + value[i + 1], value[i + 1]))
    # print(dp)
print(max(dp))
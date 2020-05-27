import sys

t = int(sys.stdin.readline())
value = list(map(int, sys.stdin.readline().split()))
dp = [0] * 1001

for i in range(t):
    min = 0
    for j in range(0, i):
        print(value[i], value[j], i, j, 'i, j')
        if value[i] > value[j]:
            # print(min, dp[j])
            if min < dp[j]:
                # print(j)
                # print(value[i], dp[j])
                min = dp[j]
                print(dp[j], 'asdf')
                # print(min)

    dp[i] = min + 1
    print(dp[i])

print(max(dp))
# print(value)
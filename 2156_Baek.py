import sys

dp = [0] * 10001
values = []

first = int(sys.stdin.readline())
for i in range(first):
    num = int(sys.stdin.readline())
    values.append(num)

if first >= 1:
    dp[0] = values[0]
elif first >= 2:
    dp[1] = values[0] + values[1]
elif first >= 3:
    dp[2] = max(dp[1], max(values[0] + values[2], values[1] + values[2]))

for i in range(1, first):
    # drink first, third, and fourth vs drink first, second, and fourth
    dp[i] = max(dp[i - 3] + values[i - 1] + values[i],  dp[i - 2] + values[i])
    # drink last glass of wine vs drink the two before the last glass
    dp[i] = max(dp[i], dp[i-1])

print(dp[first - 1])
print(dp)
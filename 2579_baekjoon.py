import sys

t = int(sys.stdin.readline())
arr = []
dp = []

for _ in range(t):
    arr.append(int(sys.stdin.readline()))

dp.append(arr[0])

if t == 2:
    dp.append(arr[0] + arr[1])

if t > 2:
    for i in range(1, 3):
        if i == 1:
            # see if arr[0] + arr[1] is bigger than arr[1]
            dp.append(max(dp[i - 1] + arr[i], arr[i]))
        # see if arr[0] + arr[2] > arr[1] + arr[2]
        else:
            dp.append(max(dp[i - 2] + arr[i], arr[i - 1] + arr[i]))

    for j in range(3, t):
        dp.append(max(arr[j] + dp[j - 2], arr[j] + arr[j - 1] + dp[j - 3]))

print(dp[-1])

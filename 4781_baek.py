import sys

while True:
    dp = [0] * 10001
    price_list = [0] * 5001
    calories_list = [0] * 5001

    num, m = map(float, sys.stdin.readline().split())
    n = int(num)
    total_cash = int(m * 100)

    if n == 0 and m == 0:
        exit()

    for _ in range(n):
        c, p = map(float, sys.stdin.readline().split())
        price = int(p * 100)
        calories = int(c)
        price_list.append(price)
        calories_list.append(calories)
    ans = 0
    for i in range(total_cash):
        for j in range(n):
            if i - price_list[j] < 0:
                continue
            else:
                dp[i] = max(dp[i], dp[i - price_list[j]] + calories_list[j])
        ans = max(ans, dp[i])

    print(ans)



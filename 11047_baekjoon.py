import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
answer = 0
counter = 0

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

for i in range(len(coins) - 1, -1, -1):
    num_coins = k // coins[i]
    counter += num_coins
    k -= num_coins * coins[i]
    if k == 0:
        print(counter)
        exit()
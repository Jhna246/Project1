import sys

price = []
weight = []
bag = []
temp_price = []
n, k = map(int, sys.stdin.readline().split())
wp = [[0 for i in range(k)] for j in range(n)]

for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    weight.append(m)
    price.append(v)

for i in range(k):
    for j in range(n):
        wp[j] = price[j], weight[j]


for _ in range(k):
    c = int(sys.stdin.readline())
    bag.append(c)

# for i in range(len(bag)):
reverse_list = (sorted(wp, reverse = True))
print(reverse_list)

for i in range(k):
    for j in range(n):
        print(reverse_list[i][0])
        continue
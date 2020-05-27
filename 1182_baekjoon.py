import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
value = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(1, len(value) + 1):
    for comb in combinations(value, i):
        # print(comb)
        sums = sum(comb)
        if sums == s:
            count += 1
        #     print(count, 'count')
        # print(sums, 'sum')
print(count)

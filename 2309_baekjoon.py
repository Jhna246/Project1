import sys
from itertools import combinations

value = []

for _ in range(9):
    value.append(int(sys.stdin.readline()))

for i in range(1, len(value) + 1):
    for comb in combinations(value, 7):
        sums = sum(comb)
        if sums == 100:
            for i in list(sorted(comb)):
                print(i)
            exit()

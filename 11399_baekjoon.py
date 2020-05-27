import sys
from itertools import permutations
from itertools import accumulate

t = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))
sorted = sorted(values)
print(sum(list(accumulate(sorted))))

# perm = permutations(values, t)
# answer = []
#
# for i in list(perm):
#     answer.append(sum(list(accumulate(i))))
# print(min(answer))

# answer = []
# for i in list(perm):
#     sum = 0
#     temp = 0
#     total = 0
#     for j in i:
#         temp = j
#         sum = sum + temp
#         total += sum
#     answer.append(total)

# print(min(answer))
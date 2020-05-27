# import sys
#
# n = int(sys.stdin.readline())
#
# while n > 0:
#     a = int(sys.stdin.readline())
#     round = 1
#     count = 0
#     lock = [0] * a
#     pos = []
#
#     for i in range(a):
#         i += 1
#         pos.append(i)
#
#     # there are a amount of rounds
#     for i in range(a):
#         # round 1 he unlocks every door
#         if round == 1:
#             for i in range(a):
#                 lock[i] = 0
#         # round 2 and above, he visits every roundth number of cells
#         if round >= 2:
#             for i in range(a):
#                 # pos[i] % round. if that is 0 that means the cell is in the roundth number
#                 if pos[i] % round == 0:
#                     # if door is locked
#                     if lock[i] == 1:
#                         lock[i] = 0
#                     # if door is unlocked
#                     else:
#                         lock[i] = 1
#         round += 1
#
#     for i in range(a):
#         if lock[i] == 0:
#             count += 1
#
#     print(count)
#
#     n -= 1
#     if n == 0:
#         exit()
#

from itertools import accumulate
door = [False for _ in range(101)]
for i in range(1, 101):
    for j in range(1, 101):
        if j % i == 0:
            door[j] = not door[j]

door = list(accumulate(door))
for _ in range(int(input())):
    print(f'{door[int(input())]}\n')
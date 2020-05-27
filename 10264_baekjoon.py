import sys

t = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
value = sorted(n)
count = 0
weight = 0

while value:
    max_num = value[-1]
    if max_num - weight > len(value):
        value.pop()
    else:
        weight += 1
        while value and value[0] - weight <= 0:
            value.pop(0)
    count += 1
print(count)

# seen = {}
#
# for i in range(len(value)):
#     n = value[i]
#     if n <= t:
#         if n in seen:
#             t -= 1
#             continue
#         else:
#             seen[value[i]] = True
#
# print(t)

# sort_value = sorted(value)
# # print(sort_value)
# i = 0
# count = 0
# while i < len(sort_value):
#     n = sort_value[i]
#     if n <= t:
#         while n in sorted(sort_value):
#             sort_value.remove(n)
#             # print(sort_value)
#             continue
#         count += 1
#     else:
#         sort_value.remove(n)
#         count += 1
# print(count)